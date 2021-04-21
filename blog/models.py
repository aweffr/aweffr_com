import os
from pathlib import Path
from django.conf import settings
from django.db import models
import uuid
import markdown
from PIL import Image
from django.utils.timezone import localtime
from django.utils import timezone
import bs4


def get_uploaded_filename(instance, filename):
    path = "protected/images/{}_{}".format(uuid.uuid4(), filename)
    return path


def convert_to_markdown(text):
    html = markdown.markdown(text, extensions=['markdown.extensions.fenced_code'])
    soup = bs4.BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("img"):
        tag["class"] = "w-100"
    return soup.prettify()


class UploadedImage(models.Model):
    """An image uploaded to the site, by an author."""
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_uploaded_filename, height_field='height', width_field='width')

    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "图片"

    def __str__(self):
        return f'<图片 id={self.id} create_at={localtime(self.create_at)}>'

    def get_with_size(self, size: int):
        name, ext = os.path.splitext(self.image.name)
        file_with_size = name + "@" + str(size) + ext
        p = Path(Path(settings.MEDIA_ROOT) / file_with_size)
        if p.exists():
            return file_with_size

        im = Image.open(self.image.path)
        origin_width = im.width
        origin_height = im.height

        if origin_height >= origin_width and origin_height > size:
            new_height = size
            new_width = int((size / origin_height) * origin_width)
            im = im.resize((new_width, new_height), resample=Image.LANCZOS, reducing_gap=3)
        elif origin_width > origin_height and origin_width > size:
            new_width = size
            new_height = int((size / origin_width) * origin_height)
            im = im.resize((new_width, new_height), resample=Image.LANCZOS, reducing_gap=3)

        new_im = im.convert("RGB")
        new_im.save(p, "JPEG", quality=settings.IMAGE_COMPRESS_QUALITY, optimize=True)

        return file_with_size


class RelatedLink(models.Model):
    name = models.CharField(max_length=255, verbose_name="连接名")
    link = models.CharField(max_length=255, verbose_name="连接")

    class Meta:
        verbose_name = verbose_name_plural = "相关链接"


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    slug = models.SlugField(max_length=255, verbose_name="slug", unique=True)

    is_published = models.BooleanField(default=False, verbose_name="已发表")
    time_published = models.DateTimeField(blank=True, null=True, verbose_name="发表时间")
    time_modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    abstract_markdown = models.TextField(blank=True, verbose_name="摘要")
    content_markdown = models.TextField(blank=True, verbose_name="正文")

    related_links = models.ManyToManyField(RelatedLink, related_name="+")

    @property
    def abstract_html(self):
        return convert_to_markdown(self.abstract_markdown)

    @property
    def content_html(self):
        return convert_to_markdown(self.content_markdown)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_published and self.time_published is None:
            self.time_published = timezone.now()

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = verbose_name_plural = "随笔"


class Tweet(models.Model):
    text = models.TextField(blank=False, verbose_name="正文")
    image = models.ForeignKey(UploadedImage, on_delete=models.SET_NULL, related_name="+", blank=True, null=True, verbose_name="配图")

    create_at = models.DateTimeField(auto_now_add=True)

    @property
    def text_html(self):
        return convert_to_markdown(self.text)

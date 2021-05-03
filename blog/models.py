import os
from pathlib import Path
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
import uuid
import markdown
from PIL import Image
from django.urls import reverse
from django.utils.timezone import localtime
from django.utils import timezone
import bs4


def get_uploaded_filename(instance, filename):
    name, ext = os.path.splitext(filename)
    path = "protected/images/{}{}".format(instance.id, ext)
    return path


def convert_markdown_to_html(text):
    html = markdown.markdown(text, extensions=['markdown.extensions.fenced_code'])
    soup = bs4.BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("img"):
        tag["class"] = "w-100"
    return soup.prettify()


class UploadedFile(models.Model):
    slug = models.SlugField(max_length=160, verbose_name="slug", unique=True)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="files/")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "文件"


class UploadedImage(models.Model):
    """An image uploaded to the site, by an author."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=get_uploaded_filename, height_field='height', width_field='width')

    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "图片"

    @property
    def url(self):
        return reverse("view_image", kwargs={"slug": self.id})

    @property
    def title_or_empty(self):
        if self.title:
            return self.title
        else:
            return "无标题"

    def __str__(self):
        return f'{self.title_or_empty} {localtime(self.create_at)}'

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

    @property
    def type(self):
        if "www.zhihu.com" in self.link:
            return "zhihu"
        elif "bilibili.com" in self.link:
            return "bilibili"
        elif "youtube.com" in self.link:
            return "youtube"
        return ""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "相关链接"


class Article(models.Model):
    TYPE_ARTICLE = "ARTICLE"
    TYPE_ARCHIVE = "ARCHIVE"
    TYPE_STUDY = "STUDY"

    TYPE_CHOICES = (
        (TYPE_ARTICLE, TYPE_ARTICLE),
        (TYPE_ARCHIVE, TYPE_ARCHIVE),
        (TYPE_STUDY, TYPE_STUDY),
    )

    SOURCE_MINE = "原创"
    SOURCE_BILIBILI = "bilibili"
    SOURCE_ZHIHU = "知乎"
    SOURCE_CAIXIN = "财新"
    SOURCE_TECH_CONF = "技术演讲"
    SOURCE_YOUTUBE = "youtube"
    SOURCE_MOOC = "公开课"
    SOURCE_OTHER = "其他"

    SOURCE_CHOICES = (
        (SOURCE_MINE, SOURCE_MINE),
        (SOURCE_BILIBILI, SOURCE_BILIBILI),
        (SOURCE_ZHIHU, SOURCE_ZHIHU),
        (SOURCE_CAIXIN, SOURCE_CAIXIN),
        (SOURCE_TECH_CONF, SOURCE_TECH_CONF),
        (SOURCE_YOUTUBE, SOURCE_YOUTUBE),
        (SOURCE_MOOC, SOURCE_MOOC),
        (SOURCE_OTHER, SOURCE_OTHER),
    )

    title = models.CharField(max_length=255, verbose_name="标题")
    slug = models.SlugField(max_length=255, verbose_name="slug", unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    media_img = models.ForeignKey(UploadedImage, on_delete=models.SET_NULL, related_name="+", blank=True, null=True, verbose_name="封面配图")
    video_iframe = models.TextField(blank=True, verbose_name="视频iframe")

    type = models.CharField(max_length=160, choices=TYPE_CHOICES, default=TYPE_ARTICLE, verbose_name="类型")
    source = models.CharField(max_length=160, choices=SOURCE_CHOICES, default=SOURCE_MINE, verbose_name="来源")
    study_subject = models.ForeignKey(
        "blog.StudySubject", related_name="notes",
        on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name="课题")

    is_published = models.BooleanField(default=False, verbose_name="已发表")
    time_published = models.DateTimeField(blank=True, null=True, verbose_name="发表时间")
    time_modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    abstract_markdown = models.TextField(blank=True, verbose_name="摘要")
    content_markdown = models.TextField(verbose_name="正文")

    related_links = models.ManyToManyField(RelatedLink, related_name="+", blank=True, verbose_name="相关链接")
    related_files = models.ManyToManyField(UploadedFile, related_name="+", blank=True, verbose_name="附件")

    @property
    def abstract_html(self):
        return convert_markdown_to_html(self.abstract_markdown)

    @property
    def content_html(self):
        return convert_markdown_to_html(self.content_markdown)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_published and self.time_published is None:
            self.time_published = timezone.now()

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.type} {self.title}'

    class Meta:
        verbose_name = verbose_name_plural = "随笔"


class Tweet(models.Model):
    text = models.TextField(blank=False, verbose_name="正文")
    image = models.ForeignKey(UploadedImage, on_delete=models.SET_NULL, related_name="+", blank=True, null=True, verbose_name="配图")
    related_links = models.ManyToManyField(RelatedLink, related_name="+", blank=True, verbose_name="相关链接")
    is_public = models.BooleanField(verbose_name="公开", default=True)

    create_at = models.DateTimeField(auto_now_add=True)

    @property
    def text_html(self):
        if self.text == "":
            return ""
        return convert_markdown_to_html(self.text)

    def __str__(self):
        if len(self.text) > 25:
            return self.text[:25] + "..."
        else:
            return self.text

    class Meta:
        ordering = ("-create_at",)
        verbose_name = verbose_name_plural = "碎碎念"


class StudySubject(models.Model):
    TYPE_BOOK = "书"
    TYPE_MOOC = "公开课"
    TYPE_TECH_CONF = "技术演讲"
    TYPE_OTHER = "其他"

    TYPE_CHOICES = (
        (TYPE_BOOK, TYPE_BOOK),
        (TYPE_MOOC, TYPE_MOOC),
        (TYPE_TECH_CONF, TYPE_TECH_CONF),
        (TYPE_OTHER, TYPE_OTHER),
    )

    type = models.CharField(max_length=160, choices=TYPE_CHOICES, default=TYPE_OTHER)
    title = models.CharField(max_length=255)
    image = models.ForeignKey(UploadedImage, on_delete=models.SET_NULL, related_name="+", blank=True, null=True, verbose_name="配图")
    related_links = models.ManyToManyField(RelatedLink, related_name="+", blank=True, verbose_name="相关链接")

    cnt_current = models.IntegerField(verbose_name="当前进度")
    cnt_total = models.IntegerField(verbose_name="总量")

    detail_markdown = models.TextField(blank=True, verbose_name="详情")
    review_markdown = models.TextField(blank=True, verbose_name="评论")
    related_files = models.ManyToManyField(UploadedFile, related_name="+", blank=True, verbose_name="附件")

    time_modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    @property
    def detail_html(self):
        if self.detail_markdown == "":
            return ""
        return convert_markdown_to_html(self.detail_markdown)

    @property
    def review_html(self):
        if self.review_markdown == "":
            return ""
        return convert_markdown_to_html(self.review_markdown)

    def __str__(self):
        return f"{self.type} {self.title}"

    class Meta:
        verbose_name = verbose_name_plural = "学习"

import os
from pathlib import Path
from django.conf import settings
from django.db import models
import uuid
import markdown
from PIL import Image


def get_uploaded_filename(instance, filename):
    path = "protected/images/{}_{}".format(uuid.uuid4(), filename)
    return path


class UploadedImage(models.Model):
    """An image uploaded to the site, by an author."""
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_uploaded_filename, height_field='height', width_field='width')

    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "图片"

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


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, editable=False)

    is_published = models.BooleanField(default=False)
    time_published = models.DateTimeField(blank=True, null=True)
    time_modified = models.DateTimeField(auto_now=True)
    content_markdown = models.TextField(blank=True)

    @property
    def content_html(self):
        return markdown.markdown(self.content_markdown, extensions=['markdown.extensions.fenced_code'])

    class Meta:
        verbose_name = verbose_name_plural = "随笔"

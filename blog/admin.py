from django.contrib import admin
from .models import UploadedImage, RelatedLink, Article, Tweet


# Register your models here.
@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    pass


@admin.register(RelatedLink)
class RelatedLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "time_modified")


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass

import logging

from django.contrib import admin
from django.http import HttpRequest

from .models import UploadedFile, UploadedImage, RelatedLink, Article, Tweet, StudySubject, Profile

logger = logging.getLogger(__name__)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ("title_or_empty", "url")
    readonly_fields = ("id", "url")


@admin.register(RelatedLink)
class RelatedLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "time_modified")

    fieldsets = (
        ['主要', {
            'fields': ('title', 'slug', 'author', 'media_img', ('type', 'source'), 'is_published', 'content_markdown'),
        }],
        ['补充', {
            'classes': ('collapse',),  # CSS
            'fields': ('video_iframe', 'time_published', 'abstract_markdown', 'related_links', 'related_files'),
        }]
    )

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        logger.debug("change=%s", change)
        if obj.author is None:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass


@admin.register(StudySubject)
class TaskAdmin(admin.ModelAdmin):
    pass

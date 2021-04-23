from django.contrib import admin
from .models import UploadedFile, UploadedImage, RelatedLink, Article, Tweet, Task


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    pass


@admin.register(RelatedLink)
class RelatedLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "time_modified")

    fieldsets = (
        ['主要', {
            'fields': ('title', 'slug', 'media_img', ('type', 'source'), 'is_published', 'content_markdown'),
        }],
        ['补充', {
            'classes': ('collapse',),  # CSS
            'fields': ('video_iframe', 'time_published', 'abstract_markdown', 'related_links', 'related_files'),
        }]
    )


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

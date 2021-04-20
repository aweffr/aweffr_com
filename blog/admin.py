from django.contrib import admin
from .models import UploadedImage, Post


# Register your models here.
@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

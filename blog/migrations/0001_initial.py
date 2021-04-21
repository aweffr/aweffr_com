# Generated by Django 3.2 on 2021-04-21 05:33

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('is_published', models.BooleanField(default=False, verbose_name='已发表')),
                ('time_published', models.DateTimeField(blank=True, null=True, verbose_name='发表时间')),
                ('time_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('content_markdown', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': '随笔',
                'verbose_name_plural': '随笔',
            },
        ),
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(height_field='height', upload_to=blog.models.get_uploaded_filename, width_field='width')),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
            },
        ),
    ]
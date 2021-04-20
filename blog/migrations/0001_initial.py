# Generated by Django 3.2 on 2021-04-20 15:57

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('is_published', models.BooleanField(default=False)),
                ('time_published', models.DateTimeField(blank=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('content_markdown', models.TextField(blank=True)),
            ],
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
        ),
    ]

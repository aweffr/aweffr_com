# Generated by Django 3.2 on 2021-04-21 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210421_2308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RelatedLinks',
            new_name='RelatedLink',
        ),
    ]

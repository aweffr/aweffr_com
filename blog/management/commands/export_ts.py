from argparse import ArgumentParser

from django.conf import settings
from django.core.management.base import BaseCommand

from django_typomatic import generate_ts


class Command(BaseCommand):
    help = "导出serializers"

    def handle(self, *args, **options):
        dst_dir = settings.BASE_DIR / "frontend" / "src" / "dto"
        if not dst_dir.exists():
            dst_dir.mkdir(parents=True)
        dst = dst_dir / "serializer.ts"
        generate_ts(dst, trim_serializer_output=True)

        with open(dst, "r") as f:
            content = f.read()

        content = "/* eslint-disable camelcase */\n\n" + content
        with open(dst, "w") as f:
            f.write(content)

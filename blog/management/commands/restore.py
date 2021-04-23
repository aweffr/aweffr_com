import os
import shutil
import subprocess
import sys
import tarfile
from argparse import ArgumentParser

from django.conf import settings
from django.core.management.base import BaseCommand


def is_dumped_json(member: tarfile.TarInfo):
    name = os.path.basename(member.name)
    if name.startswith("backup") and name.endswith(".json"):
        return True
    return False


def is_media(member: tarfile.TarInfo):
    if "/media/" in member.path:
        return True
    return False


class Command(BaseCommand):
    help = "备份数据和media"

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("file", action="store", nargs=1, type=str, help="backup文件")

    def handle(self, *args, **options):
        file = options['file'][0]
        dst = settings.BASE_DIR / "tmp"

        with tarfile.open(file, "r:gz") as t:
            t.extractall(settings.BASE_DIR / "tmp")

        sub_dir = os.listdir(dst)[0]
        backup_root = dst / sub_dir

        dump_file = [f for f in os.listdir(backup_root) if ".json" in f][0]
        dump_file = backup_root / dump_file

        cmd = f"{sys.executable} manage.py loaddata {dump_file}"
        subprocess.call(cmd, shell=True, cwd=str(settings.BASE_DIR))

        shutil.copytree(backup_root / "media", settings.MEDIA_ROOT, dirs_exist_ok=True)

        shutil.rmtree(settings.BASE_DIR / "tmp")

        self.stdout.write(f"restore finish! backup file: {file}")

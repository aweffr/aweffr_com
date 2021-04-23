import os
import sys
import tarfile
import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime


class Command(BaseCommand):
    help = "备份数据和media"

    def handle(self, *args, **options):
        cwd = settings.BASE_DIR
        dt = datetime.now().strftime('%Y-%m-%d')
        output_db = f"backup-{dt}.json"
        cmd = f"{sys.executable} manage.py dumpdata -o {output_db}"
        subprocess.call(cmd, shell=True, cwd=str(cwd))

        output_tar = f"backup-{dt}.tar.gz"

        with tarfile.open(output_tar, "w:gz") as t:
            t.add(output_db, arcname=f"./backup-{dt}/" + output_db)
            t.add("./media/", arcname=f"./backup-{dt}/media/")
        os.remove(output_db)

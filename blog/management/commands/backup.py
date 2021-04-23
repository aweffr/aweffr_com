import os
import sys
import tarfile
import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime
from django.core.mail import send_mail, EmailMessage
from argparse import ArgumentParser


class Command(BaseCommand):
    help = "备份数据和media"

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("--send-email", action='store_true')

    def handle(self, *args, **options):
        send_email = options['send_email']

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

        if send_email:
            msg = EmailMessage(
                f"aweffr_com-备份-{dt}",
                f"附件名: {output_tar}",
                from_email="aweffr_dev@foxmail.com",
                to=["aweffr@qq.com"],
            )
            with open(output_tar, 'rb') as f:
                msg.attach(output_tar, f.read(), "application/octet-stream")

            msg.send(fail_silently=False)

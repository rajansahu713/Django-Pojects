# myapp/management/commands/backup_db.py
import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Back up the database'
    def handle(self, *args, **kwargs):
        result = subprocess.run(['pg_dump', 'mydatabase', '-f', 'backup.sql'])
        if result.returncode == 0:
            self.stdout.write(self.style.SUCCESS('Database backup completed successfully'))
        else:
            self.stdout.write(self.style.ERROR('Database backup failed'))
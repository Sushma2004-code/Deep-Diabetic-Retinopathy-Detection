from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
class Command(BaseCommand):
    help = 'Create sample users for testing'
    def handle(self, *args, **options):
        for i in range(1,4):
            username = f'test{i}'
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password='password123')
        self.stdout.write('Created test users: test1..test3 (password: password123)')

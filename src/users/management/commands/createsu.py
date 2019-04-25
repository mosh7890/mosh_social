from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

_user = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not _user.objects.filter(username='admin').exists():
            _user.objects.create_superuser('admin',
                                           'admin@admin.com',
                                           'adminadmin', )

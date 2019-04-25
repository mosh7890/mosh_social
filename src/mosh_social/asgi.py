import django
import os
from decouple import config
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'mosh_social.settings.{config("ENV")}')

django.setup()

application = get_default_application()

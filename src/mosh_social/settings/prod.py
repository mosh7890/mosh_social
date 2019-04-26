import requests
import sentry_sdk as sentry
from .base import *
from sentry_sdk.integrations.django import DjangoIntegration


def get_ec2_instance_ip():
    try:
        ip = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.01).text
    except requests.exceptions.ConnectionError:
        return None
    return ip


AWS_LOCAL_IP = get_ec2_instance_ip()
ALLOWED_HOSTS.append(AWS_LOCAL_IP)

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': config('CONN_MAX_AGE', default=60),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('RDS_DB_NAME', default=''),
        'USER': config('RDS_USERNAME', default=''),
        'PASSWORD': config('RDS_PASSWORD', default=''),
        'HOST': config('RDS_HOSTNAME', default=''),
        'PORT': config('RDS_PORT', default=''),
        'TEST': {
            'NAME': f'test_{config("RDS_DB_NAME", default="")}',
        },
    }
}

INSTALLED_APPS.append('storages')

STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'

DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = None
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

if config('SENTRY_ENABLED', cast=bool, default=False):
    sentry.init(config('SENTRY_DSN', default=''), integrations=[DjangoIntegration()])

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 1000000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True

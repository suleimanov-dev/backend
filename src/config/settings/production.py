from .base import * # noqa

DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-secret-key')
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split()
CORS_ALLOWED_ORIGINS = os.environ.get('DJANGO_CORS_ALLOWED_ORIGINS', '').split()

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'chimneys.garagedoors.fun']

MEDIA_ROOT = '/var/www/ch_mr/media'
STATIC_ROOT = '/var/www/ch_mr/static'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
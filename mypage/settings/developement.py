from .base import *
import os

DEBUG = True

# ALLOWED_HOSTS = ['localhost',]


SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_personal_web', 
        'USER': 'postgres', 
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
DATABASES['default']['PASSWORD'] = os.environ.get('LOCAL_DB_PASS')

# MAIL

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kubousky@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
EMAIL_PORT = 587
EMAIL_USE_TLS = True





from .base import *

import django_heroku
import dj_database_url
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['jakub-parcheta.herokuapp.com', 'jakub-parcheta.net']

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Activate Django-Heroku.
django_heroku.settings(locals())
options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)
# del DATABASES['default']['OPTIONS']['sslmode']



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]





EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kubousky@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD') # in Heroku settings > reveal config Vars can add variables (.env doesnt work) 
EMAIL_PORT = 587                                    # then check it in teh console with a command Heroku config -app jakub-parcheta
EMAIL_USE_TLS = True
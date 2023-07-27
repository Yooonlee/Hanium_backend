"""
Django settings for dj_pr project.

Generated by 'django-admin startproject' using Django 3.0.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

###################################
# local.settings.json 내 value 값들을 받아들여, 현재 프로세스 환경변수 내역을 업데이트한다. 
import os

import json
from environ import Env 
from pathlib import Path 

env = Env()
BASE_DIR = Path(__file__).resolve().parent.parent
# print( "BASE_DIR = ",BASE_DIR)
try:
    with BASE_DIR.parent.joinpath("local.settings.json").open() as f:
        local_settings = json.load(f)
        for key, value in local_settings['Values'].items():
            env.ENVIRON[key] = value
except(IOError, KeyError):
    pass
###################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5(!&t(*4iz)c1k(=ygr8ivbpeoe-p7ex7uz@7rvzdg+9u8!5p+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'corsheaders',
    "whitenoise.runserver_nostatic",
    
    'blog',
    'uploader',
]

MIDDLEWARE = [
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  

    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj_pr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dj_pr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hanium',
        'USER' : 'yoonlee',
        'PASSWORD' : 'yoonlee',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'hanium',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'ENFORCE_SCHEMA': True,
#         'LOGGING': {
#             'version': 1,
#             'loggers': {
#                 'djongo': {
#                     'level': 'DEBUG',
#                     'propogate': False,                        
#                 }
#             },
#          },
#         'NAME': 'boilerplate',
#         'CLIENT': {
#             'host': '127.0.0.1',
#             'port': 27017,
#             'username': 'Yooonlee',
#             'password': "Yooonlee",
#             'authSource': 'admin',
#             'authMechanism': 'SCRAM-SHA-1'
#         }
#     }
# }

# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
#             'NAME': 'haniumcat',
#             'CLIENT': {
#                 "host": "mongodb+srv://Yooonlee:Yooonlee@boilerplate.eb2feiy.mongodb.net/?retryWrites=true&w=majority",
#                 "name": 'mytestdb',
#                 "authMechanism" : "SCRAM-SHA-1",
#             }  
#         }
# }

# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
#             'NAME': 'haniumcat',
#             'ENFORCE_SCHEMA': False,
#             'CLIENT': {
#                 "host": "mongodb+srv://Yooonlee:Yooonlee@boilerplate.eb2feiy.mongodb.net/?retryWrites=true&w=majority",
#             }  
#         }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'

STATIC_URL = os.environ.get("DJANGO_STATIC_URL", "/static/")  
STATIC_ROOT = os.environ.get("DJANGO_STATIC_ROOT", "./static/")  
STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

# 미디어 경로를 추가
MEDIA_URL = '/media/' 
MEDIA_ROOT = BASE_DIR.parent / 'media'

STATICFILES_STORAGE  = 'dj_pr.storages.StaticAzureStorage'
DEFAULT_FILE_STORAGE  = 'dj_pr.storages.MediaAzureStorage'

# AZURE_ACCOUNT_NAME = env.str('yooonlee0b79fa')
# AZURE_ACCOUNT_KEY = env.str('bkMC4GNh75Fi8kA+i4G5MYNrEbdSb+ysk57BO8HtS7F2K67Y3DS7paI/ytKeTh0OI/t8Ch7A1dF9+AStsL0TyQ==')


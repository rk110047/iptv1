"""
Django settings for iptv project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mnbvcxzaqwertyuioplkjhgfds'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '185.94.77.112', 
    'iptv-server-dev.us-west-2.elasticbeanstalk.com',
    '127.0.0.1', 
    'localhost'
    ]


# Application definition

#file changed
# check the file

INSTALLED_APPS = [
    #django-core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party django extensions
    'rest_framework',
    'storages',
    'authentication.apps.AuthenticationConfig',
    'liveTv.apps.LiveTvConfig',
    'archives.apps.ArchivesConfig',
    'vod.apps.VodConfig',
    'package.apps.PackageConfig',
    'radio.apps.RadioConfig',
    'settings.apps.SettingsConfig',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'authentication.User'

ROOT_URLCONF = 'iptv.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'authentication.backends.JWTAuthentication',),
    'EXCEPTION_HANDLER':
    'utils.exception_handler.custom_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'errors',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ('v1',),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

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

WSGI_APPLICATION = 'iptv.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iptv',
        'USER': 'iptv',
        'PASSWORD': 'iptv@iptv',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }

# if 'RDS_DB_NAME' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': os.environ['RDS_DB_NAME'],
#             'USER': os.environ['RDS_USERNAME'],
#             'PASSWORD': os.environ['RDS_PASSWORD'],
#             'HOST': os.environ['RDS_HOSTNAME','localhost'],
#             'PORT': os.environ['RDS_PORT'],
#         }
#     }
# else:
#     DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DB_NAME', 'iptv'),
#         'USER': os.environ.get('DB_USER', 'rk110047'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'Pankaj@705'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         # 'PORT': os.environ.get('DB_PORT', '5432'),
#     },
# }





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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# AWS_STORAGE_BUCKET_NAME = 'iptv-static'
# AWS_S3_REGION_NAME = 'us-west-2'  # e.g. us-east-2
# AWS_ACCESS_KEY_ID = 'AKIA4XGC5LI7JEYDLGXJ'  # 'AKIAIGPPSALSMHXBQ7ZA'
# 'D49FHIKGRQUGnR9WHoWZ+dkub+XtAUbF+NtmEnT4'
# AWS_SECRET_ACCESS_KEY = 'x/aELDAICuorASNpxruHahKOa3YvoSTGuuxtvybc'

# Tell django-storages the domain to use to refer to static files.
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'

# MEDIAFILES_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CORS_ORIGIN_WHITELIST = (os.environ.get('CORS_WHITELIST').split(','))

CORS_ORIGIN_ALLOW_ALL = True



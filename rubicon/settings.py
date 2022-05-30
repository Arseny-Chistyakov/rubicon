import os.path
from pathlib import Path

import dj_database_url
import django_heroku
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

load_dotenv(BASE_DIR / '.env')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blogs',
    'users',
    'products',
    'baskets',
    'orders',

    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'rubicon.urls'

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

                'rubicon.context_processors.basket',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'rubicon.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

SERVER = False
if SERVER:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('NAME'),
            'USER': os.getenv('USER'),
            'PASSWORD': os.getenv('PASSWORD'),
            'HOST': os.getenv('HOST'),
            'PORT': os.getenv('PORT'),
        }
    }
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    STATICFILES_DIRS = (BASE_DIR / 'static',)

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'W-SU' было
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

MEDIA_URL = '/media'
MEDIA_ROOT = BASE_DIR / 'media'

# MEDIA_ROOT_SHORT = 'media'
# MEDIA_URL = f'/{MEDIA_ROOT_SHORT}/'
# MEDIA_ROOT = os.path.join(BASE_DIR, f'{MEDIA_ROOT_SHORT}')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Users
AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/users/login/'

LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'

# Django Heroku
django_heroku.settings(locals())

# Verification in mail
DOMAIN_NAME = 'http://mail.ru'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Для генерации ссылки в лог-файле
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

# authorization with social

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.vk.VKOAuth2',
    # 'social_core.backends.github.GithubOAuth2',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',

    'rubicon.pipelines.save_user_profile',
    # 'github_app.auth_pipeline.user',
)

# # github
# Client_ID = os.getenv('Client ID')
# Client_secrets = os.getenv('Client_secrets')

# vk
SOCIAL_AUTH_VK_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_VK_OAUTH2_KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_VK_OAUTH2_SECRET')
SOCIAL_AUTH_VK_OAUTH2_API_VERSION = '5.131'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_VK_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

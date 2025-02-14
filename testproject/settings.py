"""
Django settings for testproject project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import datetime
import os

import environ


root = environ.Path(__file__) - 1
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env(env_file=root('.env'))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zvh+vsa)c7$)(z@z7+c!c%ex1k8lqm)*6eh4l#a(t-_m@-i_9&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

CORS_ORIGIN_ALLOW_ALL = env.bool('CORS_ORIGIN_ALLOW_ALL', default=False)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'djoser',
    'corsheaders',
    'rest_framework_swagger',

    'testapp',
    'trench',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testapp.urls'
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

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

AUTH_USER_MODEL = 'testapp.User'

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(
        days=env.int('JWT_EXPIRATION_DELTA_DAYS', default=7)
    ),
}

SIMPLE_JWT = {
    'USER_ID_FIELD': 'username',
    'USER_ID_CLAIM': 'username',
}

DJOSER = {
    'SERIALIZERS': {
        'user': 'testapp.serializers.ExtendedUserSerializer',
    }
}

TRENCH_AUTH = {
    'CONFIRM_DISABLE_WITH_CODE': True,
    'CONFIRM_BACKUP_CODES_REGENERATION_WITH_CODE': True,
    'BACKUP_CODES_CHARACTERS': '0123456789',
    'MFA_METHODS': {
        'sms': {
            'VERBOSE_NAME': 'sms',
            'VALIDITY_PERIOD': 60 * 10,
            'HANDLER': 'trench.backends.twilio.TwilioBackend',
            'SOURCE_FIELD': 'phone_number',
            'TWILIO_ACCOUNT_SID': env(
                'TWILIO_ACCOUNT_SID',
                default=''
            ),
            'TWILIO_AUTH_TOKEN': env(
                'TWILIO_AUTH_TOKEN',
                default=''
            ),
            'TWILIO_VERIFIED_FROM_NUMBER': env(
                'TWILIO_VERIFIED_FROM_NUMBER',
                default='',
            ),
        },
        'email': {
            'VERBOSE_NAME': 'email',
            'VALIDITY_PERIOD': 60 * 10,
            'HANDLER': 'trench.backends.basic_mail.SendMailBackend',
            'SOURCE_FIELD': 'email',
        },
        'app': {
            'VERBOSE_NAME': 'app',
            'VALIDITY_PERIOD': 60 * 10,
            'USES_THIRD_PARTY_CLIENT': True,
            'HANDLER': 'trench.backends.application.ApplicationBackend',
        },
        'yubi': {
            'VERBOSE_NAME': 'yubi',
            'HANDLER': 'trench.backends.yubikey.YubiKeyBackend',
            'SOURCE_FIELD': 'yubikey_id',
            'YUBICLOUD_CLIENT_ID': env(
                'YUBICLOUD_CLIENT_ID',
                default=''
            ),
        }
    }

}

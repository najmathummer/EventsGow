"""
Django settings for EventsGow project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#thjmm5q$zm&rg5-f=%$2=_^%u(b6hvqlth+w=k-*yg_$8ouj9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['eventsgow.pythonanywhere.com', 'localhost', '127.0.0.1']

# BASE_URL = "localhost:8000/"
BASE_URL = "https://eventsgow.pythonanywhere.com/"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'accounts',
    'events',
    'anymail'
]
SITE_ID = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Eventsgow.com"
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
AUTH_USER_MODEL = "accounts.CustomUser"

# EMAIL_BACKEND = 'anymail.backends.sendinblue.EmailBackend'
# ANYMAIL = {
#     'SENDINBLUE_API_KEY': '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',
#     'SENDINBLUE_API_URL': 'https://api.sendinblue.com/v3/'
# }


# DEFAULT_FROM_EMAIL = 'EventsGOW <no-reply@eventsgow.com>'
# EMAIL_USE_TLS = True

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "noreply.eventsgow@gmail.com"
EMAIL_HOST_PASSWORD = 'Hellothere123!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


ACCOUNT_ADAPTER = 'accounts.adapter.DefaultAccountAdapterCustom'
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EventsGow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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
ACCOUNT_FORMS = {'login': 'accounts.forms.MyCustomLoginForm',
                'signup': 'accounts.forms.MyCustomSignupForm',
                'reset_password': 'accounts.forms.MyCustomResetPasswordForm',

}
WSGI_APPLICATION = 'EventsGow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
LOGIN_REDIRECT_URL = 'events:home'

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = '/static/'

# Media Files
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

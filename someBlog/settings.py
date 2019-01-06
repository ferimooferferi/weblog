"""
Django settings for someBlog project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Also put your secret key in a file called secret_key.txt and paste it to your etc/djangoWebblogConf folder.
with open('/etc/djangoWebblogConf/secret_key.txt') as f:
    SECRET_KEY = f.read().strip() 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

CSRF_COOKIE_SECURE = False

#SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

ALLOWED_HOSTS = ['*']

# Enter site admins email
ADMINS = ['fuckshit@cliptik.net']

# Email configurations
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Create a file named emailConf.txt and put it in the following path. This file should contain this 
# configurations with the same order as here.
with open('/etc/djangoWebblogConf/emailConf.txt') as f:
    SERVER_EMAIL = f.readline().split('=')[1].strip()
    EMAIL_HOST = f.readline().split('=')[1].strip()
    EMAIL_HOST_USER = f.readline().split('=')[1].strip()
    EMAIL_HOST_PASSWORD = f.readline().split('=')[1].strip()
    EMAIL_PORT = f.readline().split('=')[1].strip()
    EMAIL_USE_TLS = f.readline().split('=')[1].strip()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weblog'
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

ROOT_URLCONF = 'someBlog.urls'

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

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

WSGI_APPLICATION = 'someBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# Edit your my.cnf file in the following path to connect to the MySQL database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Media files
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-MEDIA_URL

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
# Path to where collectstatic would store the static files. In production run this command.
STATIC_ROOT = ''
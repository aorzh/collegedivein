import os

PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Karambir Singh Nain', 'akarambir@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'maintest.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',
)


THIRD_PARTY_APPS = (
    'bootstrap_toolkit',
    'bootstrapform',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'gunicorn',
    'guardian',
    'django_extensions',
    'south',
)

LOCAL_APPS = (
    'student',
    'college',
    'event',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/media/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    os.path.join(PROJECT_ROOT, 'static'),
)

TEMPLATE_DIRS = (
        #os.path.join(PROJECT_ROOT, 'templates', 'allauth'),
        #os.path.join(PROJECT_ROOT, 'templates', 'cdi'),
        os.path.join(PROJECT_ROOT, 'templates'),
)

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
AUTHENTICATION_BACKENDS = (
        'allauth.account.auth_backends.AuthenticationBackend',
        'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.request',
        'django.contrib.messages.context_processors.messages',
        'allauth.account.context_processors.account',
        'allauth.socialaccount.context_processors.socialaccount',
        'event.context_processors.navigation',
)

SECRET_KEY = '@$=cchgnx5&amp;3=k+ew%(s4au=)ys048&amp;#^$%bzqs1vqw=x#$p6#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cdi.urls'
WSGI_APPLICATION = 'cdi.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SITE_ROOT_URI = 'http://collegedive.herokuapp.com/'
STATIC_URL = SITE_ROOT_URI + 'media/'

try:
    from local_settings import *
except ImportError:
    pass

try:
    from local_db_settings import *
except ImportError:
    pass

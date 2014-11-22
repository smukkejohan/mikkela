# coding=utf-8
import os.path
import sys
import platform
import django.conf.global_settings as DEFAULT_SETTINGS

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_PATH)
sys.path.append(BASE_PATH + '/apps')

ADMINS = (('Johan Bichel Lindegaard', 'mr.bichel@gmail.com'))
MANAGERS = ADMINS

DEVELOPMENT_MODE = (platform.node() != "tango")

if DEVELOPMENT_MODE:
    DEBUG = True
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = 'dev.db'
    CACHE_BACKEND = 'dummy:///'
else:
    DEBUG = False
    MEDIA_URL = 'http://media.mikkelandersen.dk/'
    STATIC_URL = 'http://static.mikkelandersen.dk/'
    ADMIN_MEDIA_PREFIX = MEDIA_URL + '/admin/'

INTERNAL_IPS = ['127.0.0.1',]
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'dk-DK'
SITE_ID = 1
USE_I18N = False

DATETIME_FORMAT = 'd/m - Y H:i'
DATE_FORMAT = 'd/m - Y'
TIME_FORMAT = 'H:i'

ALLOWED_HOSTS = ['mikkelandersen.dk']

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Static files
MEDIA_ROOT = BASE_PATH + '/../media'
STATIC_ROOT = BASE_PATH + '/../static_build'
STATICFILES_DIRS = (
    BASE_PATH + '/../static',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)


ROOT_URLCONF = 'mikkela.urls'

TEMPLATE_DIRS = (
    BASE_PATH + '/templates/',
)

INSTALLED_APPS = (

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',

    'cal',
    'testimonials',

)





try:
    execfile(BASE_PATH + '/settings_local.py')
except IOError:
    sys.stderr.write("\nYou need to copy settings_local.example to settings_local.py and customize it.\n")
    sys.exit(1)

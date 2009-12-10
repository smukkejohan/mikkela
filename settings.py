import os.path, platform

ADMINS = (('Johan Bichel Lindegaard', 'mr.bichel@gmail.com'))
MANAGERS = ADMINS

DEVELOPMENT_MODE = (platform.node() != "li140-9")

if DEVELOPMENT_MODE:
    DEBUG = True    
    MEDIA_URL = '/m/'
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = 'dev.db'
    CACHE_BACKEND = 'dummy:///'
else:
    DEBUG = False
    MEDIA_URL = 'http://static.mikkelandersen.dk/'
    ADMIN_MEDIA_PREFIX = MEDIA_URL + '/admin/'
    DATABASE_ENGINE = 'postgresql_psycopg2'
    DATABASE_USER = 'mikkel'
    DATABASE_NAME = 'mikkel_db'
    
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'dk-DK'
SITE_ID = 1
USE_I18N = False

DATETIME_FORMAT = 'd/m - Y H:i'
DATE_FORMAT = 'd/m - Y'
TIME_FORMAT = 'H:i'


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'mikkel.urls'

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), "templates")]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'mikkel.cal',
    'mikkel.testimonials',
)

# import sensitive information,
try:
   from local_settings import *
except ImportError:
   pass

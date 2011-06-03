# Django settings for wipkipvinder project.
import os.path, sys
sys.path.append('lib')

PROJECT_ROOT = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

TEMPLATE_DIRS = (
  os.path.join(PROJECT_ROOT, 'templates'),
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Tijs Teulings', 'tteulings@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl-NL'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

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
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'playthings',
    'south',
)

# Mapping city JSON format to local DB fields
# 3 cheers for old-skool DB field names (do i hear an Oracle?)
MAPPING = {
    'Den Haag' : {
        'ref' : 'MSLINK',
        'neighbourhood' : 'STADSDEEL',
        'street' : 'STRAATNAAM',
        'category' : 'TOESTELGRO',
        'type' : 'NAAM',
    },
    'Rotterdam' : {
        'ref' : 'ID_TOESTEL',
        'neighbourhood' : 'BUURTNAAM',
        'street' : 'STRAATNAAM',
        'category' : 'SOORT',
        'type' : 'TYPE',
    }
}

try:
   from local_settings import *
except ImportError:
   pass
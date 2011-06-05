from unipath import FSPath as Path
import sys
sys.path.append('lib')

PROJECT_DIR = Path(__file__).absolute().ancestor(2)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Tijs Teulings', 'tteulings@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'nl-nl'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = PROJECT_DIR.parent.child('data')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(PROJECT_DIR.child('static')),
)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'IQ65E0Gt4icQR13fP4s9739qc5ist896'

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

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'epio_commands',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'playthings',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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
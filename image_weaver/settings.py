from pathlib import Path

from corsheaders.defaults import default_headers
from decouple import Csv, config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'descriptions',
    'images',
    'users',
    # packages
    'django.contrib.postgres',
    'log_viewer',
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

ROOT_URLCONF = 'image_weaver.urls'

AUTH_USER_MODEL = 'users.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'image_weaver.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'HOST': config('DB_HOST', default=''),
        'PORT': config('DB_PORT', default=''),
    }
}

CACHE_KEY_PREFIX = config('CACHE_KEY_PREFIX', default='image_weaver')

CACHES = {
    'default': {
        'BACKEND': config('CACHE_BACKEND', default='django_redis.cache.RedisCache'),
        'KEY_PREFIX': CACHE_KEY_PREFIX,
        'LOCATION': 'redis://:{password}@{hostname}:{port}/{db_number}'.format(
            password=config('REDIS_CACHE_PASSWORD'),
            hostname=config('REDIS_CACHE_HOST', default='localhost'),
            port=config('REDIS_CACHE_PORT', default='6379'),
            db_number=config('CACHE_REDIS_DB_NUMBER', default='0')
        ),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '%sstatic/' % config('BASE_URL')

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '%smedia/' % config('BASE_URL')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery
CELERY_RESULT_BACKEND = 'redis://{username}:{password}@{host}:{port}/{db}'.format(
    username=config('CELERY_RESULT_BACKEND_USERNAME'),
    password=config('CELERY_RESULT_BACKEND_PASSWORD'),
    host=config('CELERY_RESULT_BACKEND_HOST', default='localhost'),
    port=config('CELERY_RESULT_BACKEND_PORT', default='6379'),
    db=config('CELERY_RESULT_BACKEND_DB', default='1')
)

CELERY_BROKER_URL = '{protocol}://{username}:{password}@{host}:{port}/{vhost}'.format(
    protocol=config('CELERY_BROKER_PROTOCOL', default='amqp'),
    username=config('CELERY_BROKER_USERNAME'),
    password=config('CELERY_BROKER_PASSWORD'),
    host=config('CELERY_BROKER_HOST', default='localhost'),
    port=config('CELERY_BROKER_PORT', default='5672'),
    vhost=config('CELERY_BROKER_VHOST', default='image_weaver'),
)
CELERY_TASK_ALWAYS_EAGER = config('CELERY_TASK_ALWAYS_EAGER', default=False, cast=bool)

# Constance

CONSTANCE_DATABASE_PREFIX = 'constance_image_weaver'
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_ADDITIONAL_FIELDS = {
    'decimal_field': ['django.forms.DecimalField', {}],
    'integer_field': ['django.forms.IntegerField', {}],
    'image_field': ['django.forms.ImageField', {}],
    'char_field': ['django.forms.CharField', {}],
    'email_field': ['django.forms.EmailField', {}],
    'url_field': ['django.forms.URLField', {}],
    'bool_field': ['django.forms.BooleanField', {}],
    'int_field': ['django.forms.IntegerField', {}],
    'pass_field': ['django.forms.CharField', {'widget': 'django.forms.PasswordInput'}],
}

CONSTANCE_CONFIG = {
    'EXAMPLE': (30, _('example'), 'int_field'),
}

# EMAIL

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_FROM = config('EMAIL_FROM', default='')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_TIMEOUT = config('EMAIL_TIMEOUT', default=30, cast=int)

# Cors

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = default_headers

# Log Viewer

LOG_VIEWER_FILES = []
LOG_VIEWER_FILES_PATTERN = '*.log*'
LOG_VIEWER_FILES_DIR = 'logs/'
LOG_VIEWER_PAGE_LENGTH = 25  # total log lines per-page
LOG_VIEWER_MAX_READ_LINES = 1000  # total log lines will be read
LOG_VIEWER_FILE_LIST_MAX_ITEMS_PER_PAGE = 100  # Max log files loaded in Datatable per page
LOG_VIEWER_PATTERNS = ['[20']
LOG_VIEWER_EXCLUDE_TEXT_PATTERN = None  # String regex expression to exclude the log from line

# Optionally you can set the next variables in order to customize the admin:
LOG_VIEWER_FILE_LIST_TITLE = "Image Weaver Logs"

LOG_DIR = BASE_DIR / 'logs'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'file': {
            'format': '%(asctime)s %(name)-5s %(levelname)-5s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'django_requests': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'django_requests.log',
            'formatter': 'verbose'
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'info.log',
            'formatter': 'verbose',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'error.log',
            'formatter': 'verbose',
        },
        'db_queries': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'db_queries.log',
        },
        'celery_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'celery_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'celery.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_requests', ],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['db_queries', ]
        },
        'info': {
            'handlers': ['info', ],
            'level': 'INFO',
            'propagate': False,
        },
        'error': {
            'handlers': ['error', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery_console', 'celery_file', ],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

QUEUE_NAMES = {
    "GENERAL": "general",
}

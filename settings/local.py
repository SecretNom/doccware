from .base import *



ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

DEBUG = config('DEBUG')



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB',
        },
        'NAME': config('DB_NAME_LOCAL'),
        'USER': config('DB_USER_LOCAL'),
        'PASSWORD': config('DB_PASSWORD_LOCAL'),
        'HOST': config ('DB_HOST_LOCAL'),
        'PORT': config('DB_PORT_LOCAL', cast=int),

    }
}

NPM_BIN_PATH = "D:/Program Files/nodejs/npm.cmd"

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')

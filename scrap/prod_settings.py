from .settings import *
import dj_database_url

DATABASE = {
	'default': dj_database_url.config()
}

STATIC_ROOT = 'staticfiles'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FROWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
DEBUG = False

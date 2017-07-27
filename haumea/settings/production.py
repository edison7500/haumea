from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['*', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'haumea',
        'USER': 'haumea',
        'PASSWORD': 'haumea123',
        'HOST': '/tmp/mysql.sock',
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8',
            'init_command': 'SET storage_engine=INNODB',
        }
    }
}

STATIC_URL              = '//s.deepto.me/static/'
STATIC_ROOT             = '/data/haumea/static/'


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
    },
}
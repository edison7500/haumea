from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['1ww.me', 'www.1ww.me', 'api.1ww.me', ]
# ALLOWED_HOSTS = ['*', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'haumea',
        'USER': 'haumea',
        'PASSWORD': 'haumea123',
        # 'HOST': '/tmp/mysql.sock',
        'HOST': '10.136.62.181',
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8',
            'init_command': 'SET storage_engine=INNODB',
        }
    }
}

STATIC_URL              = '//static.1ww.me/static/'
STATIC_ROOT             = '/data/static/haumea/'


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
    },
}
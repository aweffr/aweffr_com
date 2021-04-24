import sys

from .base import *

DEBUG = False

# noinspection PyUnresolvedReferences
MEDIA_ROOT = "/data/aweffr_com_media/media"

db_from_env = env.db()
db_from_env["CONN_MAX_AGE"] = 30

DATABASES = {
    'default': db_from_env,
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': True,
        'BUNDLE_DIR_NAME': 'webpack_bundle/',  # must end with slash
        'STATS_FILE': Path(BASE_DIR) / 'frontend' / 'webpack-stats-prod.json',
        'POLL_INTERVAL': 0.2,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s][%(asctime)s][%(name)s][%(filename)s:%(lineno)d]%(message)s',
            'style': '%',
        },
    },
    'handlers': {
        'console': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'file': {
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': '/data/logs/aweffr_com.log'
        },
        'db': {
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': '/data/logs/db.log'
        },
    },
    'loggers': {
        'blog': {
            'level': 'INFO',
            'handlers': [
                'console',
                'file',
            ],
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'DEBUG' if LOG_DB_SQL else 'INFO',
            'handlers': ['db'],
        },
        'django': {
            'level': 'INFO',
            'handlers': [
                'console',
                'file',
            ],
        }
    },
}

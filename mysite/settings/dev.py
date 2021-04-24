import sys

from .base import *

DEBUG = True

MEDIA_ROOT = os.path.join(str(BASE_DIR), 'media')

DATABASES = {
    'default': env.db(),
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,
        'BUNDLE_DIR_NAME': 'webpack_bundle/',  # must end with slash
        'STATS_FILE': Path(BASE_DIR) / 'frontend' / 'webpack-stats-dev.json',
        'POLL_INTERVAL': 0.2,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}

INTERNAL_IPS = [
    '127.0.0.1'
]


def skip_static_requests(record):
    if isinstance(record.args[0], str) and record.args[0].startswith('GET /static/'):
        return False
    return True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        # use Django's built in CallbackFilter to point to your filter
        'skip_static_requests': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_static_requests
        }
    },
    'formatters': {
        'standard': {
            'format': '[%(levelname)s][%(asctime)s][%(name)s][%(filename)s:%(lineno)d]%(message)s',
            'style': '%',
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'db': {
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / "logs" / "db.log"
        },
        'django.server': {
            'level': 'INFO',
            'filters': ['skip_static_requests'],
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        'blog': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'DEBUG' if LOG_DB_SQL else 'INFO',
            'handlers': ['db'],
        }
    },
}

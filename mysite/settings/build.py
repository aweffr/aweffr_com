from .base import *

DEBUG = False

MEDIA_ROOT = os.path.join(str(BASE_DIR), 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite3.db',
    }
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

from .base import *

DEBUG = True

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

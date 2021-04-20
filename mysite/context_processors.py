from django.conf import settings


def get_chunks():
    if settings.DEBUG:
        return [
            'runtime-main',
            'vendors~main',
            'main',
        ]
    else:
        return [
            'runtime-main',
            'undefined',
            'main',
        ]


def js_chunks(request):
    return {
        'chunks': get_chunks()
    }

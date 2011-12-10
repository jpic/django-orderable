import posixpath # does sane URL path joining
from django.conf import settings

def is_valid(url):
    return (('://' in url) or (url.startswith('/')))

ORDERABLE_STATIC_URL = getattr(settings, 'ORDERABLE_STATIC_URL',
    settings.STATIC_URL)

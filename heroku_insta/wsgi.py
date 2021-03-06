"""
WSGI config for heroku_insta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heroku_insta.settings")

application = get_wsgi_application()
from whitenoise import WhiteNoise


# application = WhiteNoise(application)
application = WhiteNoise(application, root=settings.STATIC_ROOT)
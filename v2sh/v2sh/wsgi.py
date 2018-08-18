"""
WSGI config for v2sh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#new added 1 line: problem unable to load static files(no more required)
# The latest version of WhiteNoise removes some options which were deprecated in the previous major release:
# see http://whitenoise.evans.io/en/stable/changelog.html#v4-0
#from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "v2sh.settings")

application = get_wsgi_application()
#new added 1 line: problem unable to load static files
#application = DjangoWhiteNoise(application)



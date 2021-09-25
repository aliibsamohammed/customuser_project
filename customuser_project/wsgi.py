"""
WSGI config for customuser_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = WhiteNoise(application, root=settings.STATIC_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customuser_project.settings')

application = get_wsgi_application()

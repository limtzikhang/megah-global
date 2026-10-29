"""
WSGI config for flantech_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://djangoproject.com
"""

import os

from django.core.wsgi import get_wsgi_application

# Instructs production web servers to look at your central setting configuration file matrix
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flantech_project.settings')

application = get_wsgi_application()

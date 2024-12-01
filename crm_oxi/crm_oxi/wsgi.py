"""
WSGI config for crm_oxi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/opt/render/project/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_oxi.settings')

application = get_wsgi_application()

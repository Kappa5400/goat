"""
WSGI config for superlists project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superlists.settings')
>>>>>>> 7f777d47fb42514aeab1dc28db82375ee44209e0

application = get_wsgi_application()

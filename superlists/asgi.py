"""
ASGI config for superlists project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superlists.settings')
>>>>>>> 7f777d47fb42514aeab1dc28db82375ee44209e0

application = get_asgi_application()

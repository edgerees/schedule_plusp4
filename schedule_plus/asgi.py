import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schedule_plus.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
})

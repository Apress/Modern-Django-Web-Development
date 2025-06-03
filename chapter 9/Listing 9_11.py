#Listing 9_11: asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelproject.settings')
application = ProtocolTypeRouter({
    'http': get_asgi_application()
})

#Listing 9_13: websocket router
from django.urls import re_path
from chatApp.consumers import ChatConsumer

websocket_urlpatterns = [
re_path(r'ws/socket-server/', ChatConsumer.as_asgi()),
] 

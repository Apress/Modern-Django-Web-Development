#Listing 9_20: Single Channel 
from asgiref.sync import async_to_sync
from .models import Clients
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Make a database row with our channel name
        Clients  .objects.create(channel_name=self.channel_name)

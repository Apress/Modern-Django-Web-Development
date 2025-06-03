#Listing 9_12: Consumer class
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'chat.message',
            'message': 'Connection established!'
        }))

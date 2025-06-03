#Listing 9_28: Channels login (async)
from channels.auth import login

class ChatConsumer(AsyncWebsocketConsumer):
    ...
    async def receive(self, text_data):
        ...
        await login(self.scope, user)
        await database_sync_to_async(self.scope["session"].save)()

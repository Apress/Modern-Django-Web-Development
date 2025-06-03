#Listing 9_21: Sending message to channel
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()
async_to_sync (channel_layer.send("channel_name", {
    "type": "chat.message",
    "text": "Hello there!",
}))

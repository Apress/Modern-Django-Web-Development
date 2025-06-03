#Listing 9_4: Starting websocket server
from websockets.asyncio import server
server.serve(handler, host, port)

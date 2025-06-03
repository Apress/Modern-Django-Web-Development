#Listing 9_6: websocket Handler
async def handler(websocket):
    try:
        async for message in websocket:
            print(f"Received: {message}")
            msg=input("enter server message: ")
            await websocket.send(f"Server says: {msg}")
    except Exception as e:
        print(f"Connection closed: {e}")

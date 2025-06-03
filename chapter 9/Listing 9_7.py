#Listing 9_7: websocket server code
import asyncio
from websockets.asyncio.server import serve

async def wshandler(websocket):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            msg=input("enter server message: ")
            await websocket.send(f"Server says: {msg}")
    except Exception as e:
        print(f"Connection closed: {e}")

async def main():
    async with serve(wshandler, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())

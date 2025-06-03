#Listing 9_8: websocket client code
import asyncio
from websockets.asyncio.client import connect

async def client_logic():
    uri = "ws://localhost:8765"
    async with connect(uri) as websocket:
        print("Connected to the server. Type 'exit' to quit.")
        while True:
            # Get user input
            message = input("Enter a message: ")
            
            # Exit condition
            if message.lower() == "exit":
                print("Closing connection.")
                break
            
            # Send message to the server
            await websocket.send(message)
            print(f"Sent: {message}")

            # Wait for response from the server
            response = await websocket.recv()
            print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(client_logic())

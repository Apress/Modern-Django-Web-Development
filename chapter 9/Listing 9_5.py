#Listing 9_5: websocket server loop
    async with serve(handler, "localhost", 8765):
        await asyncio.get_running_loop().create_future()

#Listing 1_4: coroutine
import asyncio

async def asyncHello():
    print ("Hello World")

asyncio.run(asyncHello())

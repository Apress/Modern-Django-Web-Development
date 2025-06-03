#Listing 1_5: Async Hello World
import asyncio
import time

async def asyncHello():
    await asyncio.sleep(2)
    print("\tHello World")

async def main():
    for i in range(1, 4):
        print ("Iteration:", i)
        print(f"\tstarted at {time.strftime('%X')}")
        await asyncHello()
        print(f"\tfinished at {time.strftime('%X')}")

asyncio.run(main())

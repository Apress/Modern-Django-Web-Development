#Listing 6_13: async view
async def async_call():
    await asyncio.sleep(10)
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/")
        print("Response From httpbin: ", response)

    print ("async call completed..")

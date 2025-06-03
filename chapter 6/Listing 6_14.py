#Listing 6_14: sync view with helper function
def sync_call():
    time.sleep(10)
    response = httpx.get("https://httpbin.org/")
    print("Response From httpbin: ",response)
    print ("sync call completed..")
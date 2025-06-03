#Listing 4_23: function-based view with conditional request handling
def myfunction(request):
    if request.method=="GET":
        #view logic to handle GET request
        return HttpResponse("response to GET request")
    
    if request.method=="POST":
        #view logic to handle POST request
        return HttpResponse("response to POST request")

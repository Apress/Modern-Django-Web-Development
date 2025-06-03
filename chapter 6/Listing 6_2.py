#Listing 6_2: getcookie() method 
def getcookie(request):  
    user  = request.COOKIES['username']  
    return HttpResponse("Welcome back {}! ".format(user));  

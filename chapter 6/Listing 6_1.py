#Listing 6_1: setcookie() method 
def setcookie(request):
    response = HttpResponse("Cookie Set!")
    response.set_cookie('username', 'admin')
    return response

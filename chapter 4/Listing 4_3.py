#Listing 4_3: user view with parameter
def user(request, name):
    return HttpResponse(f"<h2>Hello, {name}.</h2>")

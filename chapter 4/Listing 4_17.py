#Listing 4_17: getbook view with Form object
def getbook(request):
    form = BookForm()
    context={'form' : form}
    return render(request, "bookform.html", context)

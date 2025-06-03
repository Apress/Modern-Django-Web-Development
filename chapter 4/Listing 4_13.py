#Listing 4_13: getbook view
def getbook(request):
    context={}
    return render(request, "bookform.html", context)

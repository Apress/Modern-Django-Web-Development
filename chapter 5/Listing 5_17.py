#Listing 5_17: addbook view 
from django.shortcuts import render 
def addbook(request):
    if request.method=="POST":
        data = request.POST
        title = data["title"]
        author = data["author"]
        price = data["price"]
        publisher = data["publisher"]
        doc = Book(title = title, author = author, price = price, publisher = publisher)
        
        doc.save()
         return HttpResponse("Document Successfully Added")
    else:
         return render(request, "book.html", {})

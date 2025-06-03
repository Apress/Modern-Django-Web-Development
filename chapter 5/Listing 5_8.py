#Listing 5_8: insert document with form data
def addbook(request):
    if request.method=="POST":
        data = request.POST
        id = data["id"]
        ttl = data["title"]
        auth = data["author"]
        price = data["price"]
        pub = data["publisher"]
        book = {"id":id, "title": ttl, "author":auth, "price":price, "publisher":pub}
        col.insert_one(book)
        return HttpResponse("Document Added")
    else:
         return render(request, "book.html", {})

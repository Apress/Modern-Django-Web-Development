#Listing 5_4: add book from form
def addbook(request):
    if request.method=="POST":
        with Session(engine) as session:
            data = request.POST
            ttl = data["title"]
            auth = data["author"]
            price = data["price"]
            pub = data["publisher"]
            b1 = Book(title=ttl, author=auth, price=price, publisher=pub)

            session.add(b1)
            session.commit()
            return HttpResponse("Record added")
    context={}
    return render(request, "bookform.html", context)

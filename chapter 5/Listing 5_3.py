#Listing 5_3: add Book
def addbook(request):
    with Session(engine) as session:
        b1=Book(id=1, title="Decoupled Django", author="Gagliardi", price=3874, publisher="Apress")
        session.add(b1)
        session.commit()
        return HttpResponse("New Book added")

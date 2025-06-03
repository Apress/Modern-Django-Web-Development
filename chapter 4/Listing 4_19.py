#Listing 4_19: addbook view with POST request
def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ttl = data["title"]
            auth = data["author"]
            pr = data["price"]
            pu = data["publisher"]
            b1 = Book(title=ttl, author=auth, price=pr, publisher=pu)
            b1.save()
            return HttpResponse("<h2>Book added successfully</h2>")

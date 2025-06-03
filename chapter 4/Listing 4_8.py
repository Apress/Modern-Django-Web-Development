#Listing 4_8: book view
def book(request, id):
    book = Book.objects.get(id=id)
    context = {'book' : book}
    return render(request, 'book.html', context)

#Listing 4_44: aboutbooks view
def aboutbooks(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'aboutbooks.html', context)

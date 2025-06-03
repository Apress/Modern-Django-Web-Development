#Listing 4_11: books view
from django.shortcuts import render
from .models import Book
def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

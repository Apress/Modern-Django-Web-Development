#Listing 4_35: DetailView class
from django.views.generic.detail import DetailView
class BookDetailView(DetailView):
    model = Book
    template_name = "book.html"

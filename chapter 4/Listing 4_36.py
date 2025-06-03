#Listing 4_36: ListView class
from django.views.generic.list import ListView 
class BookListView(ListView):  
    model = Book 
    template_name = "list_books.html"

    def get_context_data(self, **kwargs):
        books = Book.objects.all()
        context = {'books': books}
        return context

#Listing 4_30: CreateView
from django.views.generic import CreateView
class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = 'book_create_form.html'
    success_url = '../books/'

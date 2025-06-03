#Listing 4_32: UpdateView
from django.views.generic.edit import UpdateView 
class BookUpdateView(UpdateView):  
    model = Book  
    fields = '__all__'  
    template_name = "book_create_form.html"
    success_url = "../books/"

#Listing 4_33: DeleteView
from django.views.generic.edit import DeleteView 
class BookDeleteView(DeleteView):  
    model = Book  
    template_name = "book_confirm_delete.html"
    success_url = "../books/"

    def get_object(self):
        return Book.objects.get(author=self.kwargs['author'])

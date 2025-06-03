#Listing 4_27: TemplateView class
class IndexView(TemplateView):  
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = {"name" : 'John'}
        return context

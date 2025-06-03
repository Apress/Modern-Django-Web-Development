#Listing 4_29: TemplateView with kwargs
from django.views.generic.base import TemplateView
class IndexView(TemplateView):  
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = {"name" : self.kwargs['name']}
        return context

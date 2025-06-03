#Listing 4_24: View class example
from django.views import View  
class MyView(View):
    def get(self, request):
        #view logic to handle GET request
        return HttpResponse("response to GET request")
   
    def post(self, request):
        #view logic to handle POST request
        return HttpResponse("response to POST request")

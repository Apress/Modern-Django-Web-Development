#Listing 7_1: hello.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()  
def sayHello(request):
    return Response({"message": "Hello, world!"})

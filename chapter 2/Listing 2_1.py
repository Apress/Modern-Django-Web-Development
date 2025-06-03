#Listing 2_1: views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Hello, World. This is the home page of FirstApp.</h2>") 

def about(request):
    return HttpResponse("<h2>Know more about FirstApp.</h2>")
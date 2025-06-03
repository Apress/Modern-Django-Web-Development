#Listing 4_45: index view
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

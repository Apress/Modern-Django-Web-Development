#Listing 4_5: render() function
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

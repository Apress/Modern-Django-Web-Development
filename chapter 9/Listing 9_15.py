#Listing 9_15: index view
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'channelApp/index.html')

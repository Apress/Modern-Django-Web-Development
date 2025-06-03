#Listing 5_7: insert document
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import col
def addbook(request):
    b1 = {"id":1, "title": "Decoupled Django", "author":"Gagliardi", "price":3874, "publisher":"Apress"}
    col.insert_one(b1)
    return HttpResponse("Document added")

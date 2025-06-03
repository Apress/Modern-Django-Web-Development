#Listing 3_9 : admin.py
from django.contrib import admin

# Register your models here.
from .models import Book

admin.site.register(Book)

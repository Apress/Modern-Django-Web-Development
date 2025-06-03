#Listing 5_12: urls.py
from django.urls import path, include

from . import views

urlpatterns = [
                path('',views.index,name='index'),  
                path('addbook/', views.addbook, name='addbook'), 
                path("getbook/<id>/", views.getbook, name="getbook"),  
                path("books/<int:price>", views.books, name="books"),          
               ]

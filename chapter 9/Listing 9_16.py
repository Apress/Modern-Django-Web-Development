#Listing 9_16: urls.py (chatApp)
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
]

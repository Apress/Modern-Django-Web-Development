#Listing 7_2: urls.py in app
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('hello/',views.sayHello),
]
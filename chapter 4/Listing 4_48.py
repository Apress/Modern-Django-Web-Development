#Listing 4_48: urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
]

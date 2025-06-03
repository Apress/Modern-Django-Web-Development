#Listing 2_3: urls.py (in project)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("firstapp/", include("firstapp.urls")),
    path('admin/', admin.site.urls),
]

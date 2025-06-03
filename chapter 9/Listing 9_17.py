#Listing 9_17: URLCONF
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('channelApp.urls')),
]

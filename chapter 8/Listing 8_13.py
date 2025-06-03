#Listing 8_13 : URLCONF with AsyncGraphQLView
from django.contrib import admin
from django.urls import path
from strawberry.django.views import AsyncGraphQLView
from myapi.app import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', AsyncGraphQLView.as_view(schema=schema)),
]

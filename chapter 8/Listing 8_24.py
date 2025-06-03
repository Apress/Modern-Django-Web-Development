#Listing 8_24 : URLCONF for  graphene_django
from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),  # Enable GraphiQL interface
]

#Listing 10_27: URL route for GraphiQL
from django.contrib import admin
from django.urls import path, include

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

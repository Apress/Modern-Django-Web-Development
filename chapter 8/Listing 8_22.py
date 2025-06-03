#Listing 8_22 : DjangoObjectType
from graphene_django import DjangoObjectType
from .models import Book

# Define a GraphQL type for the Book model
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "publisher", "price")

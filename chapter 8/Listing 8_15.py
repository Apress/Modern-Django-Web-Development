#Listing 8_15 : query with strawberry_django.field()
import strawberry
@strawberry.type
class Query:
    all_books: list[BookType] = strawberry_django.field()

#Listing 8_16 : filtered query
@strawberry.input
class BookFilterInput:
    id: strawberry.ID


@strawberry.type
class Query:
    all_books: list[BookType] = strawberry_django.field()
    book_by_id: BookType | None = strawberry_django.field(filters=BookFilterInput)

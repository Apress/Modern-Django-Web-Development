#Listing 8_17 : Mutation to add book
@strawberry.type
class Mutation:
    @strawberry_django.mutation
    def create_book(self, title: str, author: str, price: int, publisher: str) -> BookType:
        return Book.objects.create(title=title, author=author, price=price, publisher=publisher)

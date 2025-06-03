#Listing 8_11 : app.py (strawberry mutation)
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str, price: int) -> Book:
        print(f"Adding new book: {title}")

        return Book(title=title, author=author, price=price)        

#Listing 8_10 : app.py (Strawberry schema)
import strawberry

@strawberry.type
class Book:
    title: str
    author: str
    price: int

@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> Book:
        return Book(title="Numerical Python", author="Johansan", price: 750)
    
schema = strawberry.Schema(query=Query)

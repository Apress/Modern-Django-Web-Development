#Listing 8_9 : Strawberry Query
@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> Book:
        return Book(title="Numerical Python", author="Johansan", price = 750  )

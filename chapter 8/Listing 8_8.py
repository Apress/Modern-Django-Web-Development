#Listing 8_8 : Strawberry type
import strawberry

@strawberry.type
class Book:
    title: str
    author: str
    price: int

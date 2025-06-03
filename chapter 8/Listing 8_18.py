#Listing 8_18 : Graphene ObjectType
import graphene

class Book(graphene.ObjectType):
    title = graphene.String()
    author = graphene.String()
    price = graphene.Int()
    publisher = graphene.String()

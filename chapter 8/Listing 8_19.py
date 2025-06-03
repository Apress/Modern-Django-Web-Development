#Listing 8_19 : Graphene query
class Query(graphene.ObjectType):
    all_books = graphene.List(Book)

#Listing 8_19 : Graphene resolver function
    # Resolver to fetch all books
    def resolve_all_books(root, info) -> List[Book]:
        return books

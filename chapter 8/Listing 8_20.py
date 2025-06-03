#Listing 8_20 : Graphene mutation
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        price = graphene.Int(required=True)
        publisher = graphene.String(required=True)

    book = graphene.Field(Book)

    def mutate(self, root  , info, title: str, author:str, price:int, publisher:str) -> "CreateBook":
        new_book = {"title": title, "author": author, "price":price, "publisher":publisher}
        books.append(new_book)
        return CreateBook(book=Book(**new_book))

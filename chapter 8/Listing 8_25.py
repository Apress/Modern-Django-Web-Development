#Listing 8_25: mutation for  graphene_django
# Define Mutations
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        publisher = graphene.String(required=True)
        price = graphene.Int(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, author, publisher, price):
        book = Book.objects.create(
            title=title, 
            author=author, 
            publisher=publisher, 
            price=price
        )
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

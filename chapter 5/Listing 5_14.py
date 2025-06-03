#Listing 5_14: Book document 
class Book(Document):
    bookId = IntField(primary_key=True)
    title = StringField(max_length=50)
    author = StringField(max_length=50)
    price = IntField()
    publisher = StringField(max_length=50)

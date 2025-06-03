#Listing 5_15: meta attribute
class Book(Document):
    bookId = IntField(primary_key=True)
    title = StringField(max_length=50)
    author = StringField(max_length=50)
    price = IntField()
    publisher = StringField(max_length=50)
    meta = {'collection': 'Books'}

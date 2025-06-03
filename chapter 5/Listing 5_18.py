#Listing 5_18: DynamicDocument
class Book(DynamicDocument):
    title = StringField(max_length=50)
    author = StringField(max_length=50)
    price = IntField()
    publisher = StringField(max_length=50)
    meta = {'collection': 'Books'}

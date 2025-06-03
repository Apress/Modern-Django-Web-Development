#Listing 5_16: MongoEngine with Django  
from mongoengine import *

con = connect('mydb')

class Book(Document):
    title = StringField(max_length=50)
    author = StringField(max_length=50)
    price = IntField()
    publisher = StringField(max_length=50)
    meta = {'collection': 'Books'}

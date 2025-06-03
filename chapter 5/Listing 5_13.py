#Listing 5_13: MongoEngine Document
from mongoengine import *

class Book(Document):
    title = StringField(max_length=50)
    author = StringField(max_length=50)
    price = IntField()
    publisher = StringField(max_length=50)

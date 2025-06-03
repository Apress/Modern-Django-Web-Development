#Listing 8_14 : models.py
from django.db import models
import strawberry_django
import strawberry

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)

    class Meta:
        db_table = "books"
    
@strawberry_django.type(Book)
class BookType:
    id: strawberry.ID 
    title: str
    author: str
    price: int
    publisher: str

#Listing 3_7 : Book model
from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)

    class Meta:
        db_table = "books"

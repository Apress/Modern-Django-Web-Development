#Listing 3_10 : Book model updated
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

    def __str__(self):
        return "Title : {} Author : {} Price : {}".format(self.title, self.author, self.price)

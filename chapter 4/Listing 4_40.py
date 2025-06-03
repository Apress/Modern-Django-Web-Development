#Listing 4_40: Book model modified
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)
    ebook = models.BooleanField(default=True)
    coverimg = models.CharField(max_length=50)
    class Meta:
        db_table = "books"

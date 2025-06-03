#Listing 3_13 : Subject model
class Subject(models.Model):
    Subjectcode = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()

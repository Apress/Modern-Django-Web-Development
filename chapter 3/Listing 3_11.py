#Listing 3_11 : College model
class College (Model):
    CollegeID = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    city=models.CharField(max_length=50)

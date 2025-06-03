#Listing 3_12 : Principal model
class Principal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    CollegeID = models.OneToOneField(
                College,
                on_delete=models.CASCADE
                )

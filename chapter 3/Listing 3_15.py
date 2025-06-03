#Listing 3_15 : Teacher model updated
class Teacher(models.Model):
    TeacherID = models.IntegerField (primary_key=True)
    name = models.EmailField(max_length=50)
    qualification = models.CharField(max_length=50)

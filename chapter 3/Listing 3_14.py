#Listing 3_14 : Teacher model
class Teacher(models.Model):
    TeacherID = models.IntegerField (primary_key=True)
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    subjectcode=models.ForeignKey(
            Subject, 
            on_delete=models.CASCADE
                )

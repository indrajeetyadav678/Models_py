from django.db import models

# Create your models here.
class Student(models.Model):
    Name= models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Add=models.CharField(max_length=100)
    City=models.CharField(max_length=50, null=True)
    class Meta:
        ordering=["-Contact"]
        # app_label="app"  #add 
        # verbose_name="stu"
        # verbose_name_plural="student"
        # db_table='stu_table'
        get_latest_by="Name"
        # db_table_comment="Question Answer"
    
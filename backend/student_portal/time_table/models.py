from django.db import models
from students.models import studentsDetails

# Create your models here.
class timtTable(models.Model):
    studentsDetails_id=models.ForeignKey(studentsDetails,null=True,on_delete=models.SET_NULL)
    branch=models.CharField(max_length=50)
    semister=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    p1=models.CharField(max_length=50)
    p2=models.CharField(max_length=50)
    p3=models.CharField(max_length=50)
    p4=models.CharField(max_length=50)
    p5=models.CharField(max_length=50)
    p6=models.CharField(max_length=50)
    p7=models.CharField(max_length=50)
    p8=models.CharField(max_length=50)
    time1=models.TimeField()
    time2=models.TimeField()
    time3=models.TimeField()
    time4=models.TimeField()
    time4=models.TimeField()
    time5=models.TimeField()
    time6=models.TimeField()
    time7=models.TimeField()
    time8=models.TimeField()

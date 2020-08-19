from django.db import models
from students.models import studentsDetails

# Create your models here.
class attendence(models.Model):
    studentsDetails_id=models.ForeignKey(studentsDetails,null=True,on_delete=models.SET_NULL)
    date=models.DateField()
    student_id=models.CharField(max_length=50,default='none')
    p1=models.CharField(max_length=50,default='none')
    p2=models.CharField(max_length=50,default='none')
    p3=models.CharField(max_length=50,default='none')
    p4=models.CharField(max_length=50,default='none')
    p5=models.CharField(max_length=50,default='none')
    p6=models.CharField(max_length=50,default='none')
    p7=models.CharField(max_length=50,default='none')
    p8=models.CharField(max_length=50,default='none')
    
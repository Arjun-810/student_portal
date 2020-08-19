from django.db import models
from students.models import studentsDetails

# Create your models here.
class marks(models.Model):
    studentsDetails_id=models.ForeignKey(studentsDetails,null=True,on_delete=models.SET_NULL)
    student_id=models.CharField(max_length=50,default='none')
    test_name=models.CharField(max_length=50,default='none')
    Mathematcs=models.CharField(max_length=50,default='none')
    Human_values=models.CharField(max_length=50,default='none')
    DS=models.CharField(max_length=50,default='none')
    COA=models.CharField(max_length=50,default='none')
    DSL=models.CharField(max_length=50,default='none')
    
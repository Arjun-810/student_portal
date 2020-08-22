from django.db import models
from students.models import studentsDetails

# Create your models here.
class attendence(models.Model):
    studentsDetails_id=models.ForeignKey(studentsDetails,null=True,on_delete=models.SET_NULL)
    date=models.DateField()
    student_id=models.CharField(max_length=50,default='none')
    pre_prcentage = models.CharField(max_length=50,default='none')
    abs_prcentage = models.CharField(max_length=50,default='none')
    pre_no = models.CharField(max_length=50,default='none')
    abs_no = models.CharField(max_length=50,default='none')
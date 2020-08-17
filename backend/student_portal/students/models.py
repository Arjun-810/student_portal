from django.db import models

# Create your models here.
class studentsDetails(models.Model):
    Name = models.CharField(max_length=50)
    Roll_no = models.CharField(max_length=50)
    mail_id = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=500)
    Branch = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    semister = models.CharField(max_length=50)
    dob= models.CharField(max_length = 200, blank=True)
    status=models.CharField(max_length=200,default="OK")
from django.db import models

# Create your models here.
class studentDetails(models.Model):
    mailId = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
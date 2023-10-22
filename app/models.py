from django.db import models
from datetime import datetime
# Create your models here.




class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=40,null=False)
    subject = models.CharField(max_length=40,null=True,blank=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(max_length=30,null=True)
    mob = models.IntegerField(default=123456,null=True)


    

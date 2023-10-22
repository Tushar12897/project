from django.db import models
from datetime import datetime
# Create your models here.




class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=40,null=False)
    subject = models.CharField(max_length=40,blank=True)
    birthday = models.DateField()
    email = models.EmailField()
    mob = models.IntegerField(default=123456)


    
 
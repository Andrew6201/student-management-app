from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    firstname = models.CharField(max_length=2000)
    lastname = models.CharField(max_length=2000)
    othernames = models.CharField(max_length=2000)
    email = models.EmailField()
    course = models.CharField(max_length=1000)  
    gpa = models.FloatField()
    address = models.CharField(max_length=3000) 
    country = models.CharField(max_length=3000)  
    mobile = models.IntegerField()  

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

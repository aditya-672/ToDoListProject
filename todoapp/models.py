from statistics import mode
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    mobno = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=50,primary_key=True) 
    password = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class TasksModel(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    priority = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    
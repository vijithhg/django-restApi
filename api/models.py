from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=15)
    age = models.CharField(max_length=2)


    def __str__(self):
        return self.name
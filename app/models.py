from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=256)
    roll = models.IntegerField()
    city = models.CharField(max_length=256)
    teacher = models.CharField(max_length=256)

from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=20)
    marks = models.FloatField()
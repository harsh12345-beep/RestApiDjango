from operator import mod
from types import coroutine
from unicodedata import name
from django.db import models

# Create your models here.

class details(models.Model):
    name = models.CharField(max_length=40)
    course = models.CharField(max_length=10) 



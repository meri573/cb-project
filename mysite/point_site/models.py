from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField()
    password = models.TextField()
    points = models.IntegerField() 
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Points(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField()
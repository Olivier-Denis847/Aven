from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    pass

class Listing(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField()
    price = models.FloatField()
    description = models.CharField(max_length=500)
    date = models.DateTimeField()
    category = models.CharField()
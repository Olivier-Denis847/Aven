from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class Listing(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField()
    description = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.datetime.now())
    category = models.CharField()

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    wishlist = models.ManyToManyField(Listing)

class Bid(models.Model):
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='active_bids')
    listing = models.OneToOneField(
        Listing, on_delete=models.CASCADE, related_name='highest_bid')

class Comment(models.Model):
    content = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')

# from tkinter import CASCADE
from django.db import models
from django.utils  import timezone
from django.contrib.auth.models import User

# Create your models here.
class NeighbourHood(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    location = models.TextField(max_length=50)


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    hood = models.ForeignKey(NeighbourHood,null=False, blank=False, on_delete=models.PROTECT )
    email = models.EmailField(null=False, blank=False)
    updated_on = models.DateTimeField(default=timezone.now)


# from tkinter import CASCADE
from ssl import PROTOCOL_TLS_CLIENT
from django.db import models
from django.utils  import timezone
from django.contrib.auth.models import User


# Create your models here.
class NeighbourHood(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    location = models.TextField(max_length=50)

    def __str__(self):
        return str(self.location)


    def save_neighborhood(self):
        self.save()
        




class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    hood = models.ForeignKey(NeighbourHood,null=False, blank=False, on_delete=models.PROTECT )
    email = models.EmailField(null=False, blank=False)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.author)



class Business(models.Model):
    name = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.PROTECT, null=False, blank=False)
    business_email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return str(self.name)
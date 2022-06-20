# from tkinter import CASCADE
from ssl import PROTOCOL_TLS_CLIENT
from django.db import models
from django.utils  import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class NeighbourHood(models.Model):
    location = models.TextField(max_length=50)

    def __str__(self):
        return str(self.location)


    def save_neighborhood(self):
        self.save()
        




class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    hood = models.ForeignKey(NeighbourHood,null=True, blank=True, on_delete=models.PROTECT )
    email = models.EmailField(null=False, blank=False)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


    

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    hood = models.CharField(max_length=255, null=False, blank=False)

    
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
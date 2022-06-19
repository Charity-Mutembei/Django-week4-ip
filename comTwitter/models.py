from django.db import models
from django.utils  import timezone
from django.contrib.auth.models import User

# Create your models here.
class NeighbourHood(models.Model):
    name = models.TextField(max_length=50)
    location = models.TextField(max_length=50)


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


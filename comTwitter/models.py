from django.db import models

# Create your models here.
class NeighbourHood(models.Model):
    name = models.TextField(max_length=50)
    location = models.TextField(max_length=50)
    


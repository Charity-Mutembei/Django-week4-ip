from django.contrib import admin
from .models import Post, UserProfile, NeighbourHood, Business

# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(NeighbourHood)
admin.site.register(Business)
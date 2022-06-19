from django.shortcuts import render
from  django.views import View
from .models import Post
from .forms import PostForm

# Create your views here.

class postListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by("-created_on")
        form  = PostForm()



        return render(request, 'landing.html', {'posts': posts, 'form': form})


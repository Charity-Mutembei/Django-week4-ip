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

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)


        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context={
                'posts': posts, 
                'form': form,
            }

        return render(request, 'landing.html', context)
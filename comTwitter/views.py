from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from  django.views import View
from django.views.generic.edit  import CreateView
from .models import Post, UserProfile
from .forms import PostForm,CreateUserForm
from .email import send_welcome_email

# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')



class postListView(CreateView):
    def get(self, request, *args, **kwargs):
        user = self.request.user.profile
        posts = Post.objects.all()
        form  = PostForm()



        return render(request, 'landing.html', {'posts': posts, 'form': form})

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)


        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = self.request.user.profile
            new_post.save()

            return redirect('landing')

        context={
            'posts': posts,
            'form': form,

        }
        return render(request, 'landing.html', context)
        

class ProfileView( CreateView):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')


        context={
            'profile': profile,
            'user': user,
            'posts': posts,
        }

        return render(request, 'profile.html', context)

class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'hood', 'email']
    template_name = 'profile_edit.html'


    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy ('profile', kwargs={'pk':pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


def Category(request, location):
    return render(request, 'category.html', {'location': location})
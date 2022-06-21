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
from .models import Post, UserProfile, Business
from .forms import PostForm,CreateUserForm, BusinessForm
from .email import send_welcome_email
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def landing(request):
    posts = Post.objects.all().order_by('-created_on')
    businesses=Business.objects.all().order_by('-created_on')
    return render(request, 'landing.html', {'posts':posts, 'businesses': businesses})

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('welcome')

def login_user(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing')

        else:
            messages.success(request, ('There was an error! Please try again'))
            return redirect('login')

    else:
        return render(request, 'auth/login.html')

def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)

            messages.success(request,('Registration successfull'))

            return redirect('landing')

    else:
        form=CreateUserForm()
    return render(request, 'auth/register.html', {'form': form})




class postListView(LoginRequiredMixin,CreateView):
    def get(self, request, *args, **kwargs):
        user = self.request.user.profile
        posts = Post.objects.all()
        form  = PostForm()



        return render(request, 'new_post.html', {'posts': posts, 'form': form})

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
        return render(request, 'new_post.html', context)
        

class ProfileView(LoginRequiredMixin, CreateView):
    def get(self, request):
        profile = request.user.profile
        user = self.request.user.profile
        posts = Post.objects.filter(author=user).order_by('-created_on')


        context={
            'profile': profile,
            'user': user,
            'posts': posts,
        }

        return render(request, 'profile.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'hood', 'email']
    template_name = 'profile_edit.html'


    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy ('profile', kwargs={'pk':pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


# def Category(request, location):
#     posts_locations=Post.objects.filter(hood=location)
#     return render(request, 'category.html', {'location': location, 'posts_locations': posts_locations})


@login_required(login_url='login')
def Category(request):
    if 'post' in request.GET and request.GET['post']:
        filter_term = request.GET.get('post')
        filtered_posts = Post.search_by_hood(filter_term)
        message = f'{filter_term}'

        return render(request, 'category.html', {'message': message, 'posts': filtered_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'category.html', {'message': message})



@login_required(login_url='login')
def business(request):
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            jobs = form.save(commit=False)
            jobs.author = request.user.profile
            jobs.save()
            messages.success(request,f'The business has been posted successfully')
            return redirect('businessshow')

    context = {'form':form}
    return render(request,'business.html',context)


def businessshow(request):
    businesses=Business.objects.all().order_by('-created_on')


    return render(request, 'new_business.html', {'businesses': businesses})
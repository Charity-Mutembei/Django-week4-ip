from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from  django.views import View
from django.views.generic.edit  import CreateView
from .models import Post
from .forms import PostForm, registrationForm

# Create your views here.
def registerPage(request):
    form = registrationForm()
    if request.method == 'POST':
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = form.save()
            login(request,user,backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect ('landing')

    return render(request, 'register.html', {'form':form})    


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('landing')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('landing')

        else:
            messages.error(request, 'Username or Password does not exist')

    context = {'page': page}
    context = {}

    return render(request, 'login.html', context)



class postListView(LoginRequiredMixin,CreateView):
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

            return redirect('landing')

        context={
            'posts': posts,
            'form': form,

        }
        return render(request, 'landing.html', context)
        


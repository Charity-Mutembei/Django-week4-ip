# from tkinter import Widget
from django import forms 
from .models import Post, NeighbourHood, Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


choices = NeighbourHood.objects.all().values_list('location', 'location')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['body','hood',]

        widget={
            'body': forms.Textarea(attrs={
                'rows': '2', 
                'placeholder': 'Whats happening...',
                } ),
            'hood':forms.Select(choices=choice_list,attrs={'class': 'form-control'}),

            }
   

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'hood', 'business_email', 'created_on',]

  
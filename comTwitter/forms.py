from django import forms 
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2', 
            'placeholder': 'Whats happening...'
        } ))
    class Meta:
        model = Post
        fields = ['body',]


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

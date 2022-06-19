from django.shortcuts import render
from  django.views import View

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

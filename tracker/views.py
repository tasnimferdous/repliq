from django.shortcuts import render
from .models import User

 #Create your views here.

def home(request):
    # log = Log.objects.all()

    context = {
    # 'logs':log,    
    }
    return render(request, 'tracker/home.html', context)

def signUp(request):
    context = {  
    }
    return render(request, 'tracker/registration.html', context)

def signIn(request):
    context = {  
    }
    return render(request, 'tracker/login.html', context)


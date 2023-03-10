from django.shortcuts import render
from .models import Company, User, Device, Log

 #Create your views here.

def home(request):
    company = Company.objects.all()

    context = {
    'companies':company,    
    }
    return render(request, 'tracker/home.html', context)

def companyInfo(request,pk):
    company = Company.objects.get(id = pk)
    employees = company.user_set.all()
    logs = company.log_set.all().order_by('-updated')
    context = {
    'logs': logs,
    'employees': employees,
    }
    return render(request, 'tracker/company_info.html', context)

def signUp(request):
    context = {  
    }
    return render(request, 'tracker/registration.html', context)

def signIn(request):
    context = {  
    }
    return render(request, 'tracker/login.html', context)


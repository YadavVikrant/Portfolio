from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("NIKAL JA BSDK")
    return render(request,'personal/home.html')

def experience(request):
    return render(request,'personal/experience.html')

def project(request):
    return render(request,'personal/project.html')

def pythn(request):
    return render(request,'personal/python.html')
    

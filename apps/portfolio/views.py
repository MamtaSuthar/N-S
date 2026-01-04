from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, 'index.html',{'PROJECT_NAME': settings.PROJECT_NAME})

def about(request):
    return render(request, 'about.html',{'PROJECT_NAME': settings.PROJECT_NAME})

def service(request):
    return render(request, 'service.html',{'PROJECT_NAME': settings.PROJECT_NAME})

def project(request):
    return render(request, 'project.html',{'PROJECT_NAME': settings.PROJECT_NAME})

def contact(request):
    return render(request, 'contact.html',{'PROJECT_NAME': settings.PROJECT_NAME})

def blog(request):
    return render(request, 'blog.html',{'PROJECT_NAME': settings.PROJECT_NAME})

def single(request):
    return render(request, 'single.html',{'PROJECT_NAME': settings.PROJECT_NAME})
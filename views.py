
from django.shortcuts import render

def welcome_view(request):
    return render(request, 'reporters/welcome.html')

# reporters/views.py
from django.shortcuts import render

def register_view(request):
    return render(request, 'reporters/register.html')

def login_view(request):
    return render(request, 'reporters/login.html')

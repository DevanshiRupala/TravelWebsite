from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def create_account(request):
    error = ""
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
            UserDetail.objects.create(email=email,username=username,password=password)
            error = "no"
        except:
            error = "yes"
    return render(request, 'signup.html',locals())

def login(request):
    error_login = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = UserDetail.objects.get(email=email,password=password)
            print(user)
            if user :
                error_login = "no"
            else:
                error_login = "yes"
        except:
            error_login = "yes"
    return render(request, 'signup.html',locals())

def home(request):
    return render(request,'home.html')

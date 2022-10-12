from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout 
from django.contrib import messages
from account.auth import BackEndSetting
from .models import NewUser

# Create your views here.
app_name = "account"

auth = BackEndSetting()

def signin(request):
    return render(request, "account/login.html")

def signout(request):
    logout(request)
    return redirect('signin')

def register(request):
     return render(request, "account/login.html")



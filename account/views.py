from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout 
from django.contrib import messages
from account.auth import BackEndSetting
from .models import NewUser

# Create your views here.
app_name = "account"

auth = BackEndSetting()

def authentication(request):
    return render(request, "account/authentication.html")

def signout(request):
    logout(request)
    return redirect('store')





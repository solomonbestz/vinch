from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout 
from django.contrib import messages
from account.auth import BackEndSetting
from .models import NewUser

# Create your views here.
app_name = "account"

auth = BackEndSetting()

def authentication(request):
    if request.method == "POST":
        first_name = request.POST.get("")
        last_name = request.POST.get("")
        middle_name = request.POST.get("")
        email = request.POST.get("")
        password1 = request.POST.get("")
        password2 = request.POST.get("")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = auth.authenticate(request, email=email, password=password)
        if user is not None and user.is_staff == False:
            login(request, user)
            if user.is_active == True:
                messages.success(request, "Successfully logged In.")
                print("User is logged in")
                return redirect("store")
            else:
                print("User is not active")
                return redirect("404")
        else:
            messages.error(request, "Incorrect Login Details")
            return redirect('signin')  
    else:
        pass
    return render(request, "account/authentication.html")

def signout(request):
    logout(request)
    return redirect('store')





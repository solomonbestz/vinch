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
        first_name = request.POST.get("f-name")
        last_name = request.POST.get("l-name")
        middle_name = request.POST.get("m-name")
        email = request.POST.get("email")
        password1 = request.POST.get("f-password")
        password2 = request.POST.get("s-password")

        print(f"{first_name} {last_name} {password1} {password2}")
    
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
            return redirect('authentication')  
    else:
        pass
    return render(request, "account/authentication.html")

def signout(request):
    logout(request)
    return redirect('store')





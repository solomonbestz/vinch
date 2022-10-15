from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib import messages
from account.auth import BackEndSetting
from .models import NewUser
import json

# Create your views here.
app_name = "account"

auth = BackEndSetting()

def authentication(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'Register':
            print("entered reg")
            try:
                first_name = request.POST.get("f-name")
                last_name = request.POST.get("l-name")
                middle_name = request.POST.get("m-name")
                email = request.POST.get("email")
                gender = request.POST.get("gender")
                password1 = request.POST.get("f-password")
                password2 = request.POST.get("s-password")

                check_email(request, email)

                if password1 == password2:
                    pass
                else:
                    return redirect("authentication")

                user = NewUser.objects.create_user(email, password1, first_name=first_name, last_name=last_name, middle_name=middle_name, gender=gender)
                user.is_active = False
                user.save()
                messages.success(request, "You have successfully registered")
                return redirect('authentication')
            except:
                return redirect('authentication')
    
        elif request.POST.get('submit') == 'Sign in':
            
            print("entered login")
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
                    return redirect("verify_404")
            else: 
                messages.error(request, "Incorrect Login Details")
                return redirect('authentication')  
        
        print("Didn't enter")

    return render(request, "account/authentication.html")

def signout(request):
    logout(request)
    return redirect('store')


def verification_404(request):
    return render(request, "account/verify_404.html")

def check_email(request, email):
    if NewUser.objects.filter(email=email):
        messages.error(request, "Email already registered! Please try some otehr Email")
        return redirect("authentication")




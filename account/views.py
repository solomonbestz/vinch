from django.http import HttpResponse
from django.utils.encoding import force_bytes
from .email import send_message
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib import messages
from account.auth import BackEndSetting
from .activation import activate_account
from .models import NewUser
from store.models import *
import json

# Create your views here.
app_name = "account"

auth = BackEndSetting()

def authentication(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'Register':
            # try:
            first_name = request.POST.get("f-name")
            last_name = request.POST.get("l-name")
            middle_name = request.POST.get("m-name")
            email = request.POST.get("email")
            gender = request.POST.get("gender")
            phone = request.POST.get("phone")
            password1 = request.POST.get("f-password")
            password2 = request.POST.get("s-password")

            check_email(request, email)

            if password1 == password2:
                pass
            else:
                return redirect("authentication")

            user = NewUser.objects.create_user(email, password1, first_name=first_name, last_name=last_name, middle_name=middle_name, gender=gender, phone_number=phone)
            user.is_active = False
            user.save()
            activate_account(request, user, email)

            messages.success(request, "You have successfully registered")
            return redirect('authentication')
            # except:
            #     return redirect('authentication')
    
        elif request.POST.get('submit') == 'Sign in':
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = auth.authenticate(request, email=email, password=password)
            if user is not None and user.is_staff == False:
                login(request, user)
                if user.is_active == True:
                    messages.success(request, "Successfully logged In.")
                    add_cart_db(request)
                    return redirect("store")
                else:
                    return redirect("verify_404")
            else: 
                messages.error(request, "Incorrect Login Details")
                return redirect('authentication')  
        
        print("Didn't enter")

    return render(request, "account/authentication.html")

def signout(request):
    logout(request)
    return redirect('store')

def ActivateAccount(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = NewUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, NewUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return HttpResponse('Your account has been activated')
    else:
        return HttpResponse('Activation link is invalid, contact admin for further help.')



def verification_404(request):
    return render(request, "account/verify_404.html")

def my_account(request):
    customer = request.user.customer
    try:
        shipping = ShippingAddress.objects.get(customer=customer)
    except:
        shipping = {}
    update_shipping_address(request, shipping)
    account = NewUser.objects.get(id = request.user.id)
    return render(request, "account/my_account.html",{"account": account, "shipping": shipping})

def my_orders(request):
    customer = request.user.customer
    order = Order.objects.filter(customer=customer, complete=True)
    return render(request, "account/my_orders.html", {'order_item': order})

def check_email(request, email):
    if NewUser.objects.filter(email=email):
        messages.error(request, "Email already registered! Please try some otehr Email")
        return redirect("authentication")

def add_cart_db(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        for i in cart:
            try:
                product = Product.objects.get(id=i) 
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)        
                orderItem.quantity = orderItem.quantity + cart[i]['quantity']
                orderItem.save()
            except:
                pass

def update_shipping_address(request, shipping):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        city = request.POST.get("city")
        address = request.POST.get('address')
        country = request.POST.get("country")
        state = request.POST.get("state")
        zipcode = request.POST.get("zip")

        shipping.first_name = firstname
        shipping.last_name = lastname
        shipping.city = city
        shipping.address = address
        shipping.country = country
        shipping.state = state
        shipping.zipcode = zipcode

        shipping.save()

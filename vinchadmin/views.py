from django.shortcuts import render
from account.models import NewUser
from store.models import *



def dashboard(request):
    return render(request, 'admindashboard/dashboard.html')

def users(request):
    user = NewUser.objects.filter()
    return render(request, 'admindashboard/users.html', {'users': user})

def customers(request):
    customer = Customer.objects.filter()
    return render(request, 'admindashboard/customers.html', {'customers': customer})
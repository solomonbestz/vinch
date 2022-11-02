from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from account.models import NewUser
from store.models import *



def dashboard(request):
    return render(request, 'admindashboard/dashboard.html')

def users(request):
    u = NewUser.objects.all()
    user = Paginator(u, 1)
    page_num = request.GET.get('page', 1)

    try:
        user = user.page(page_num)
    except EmptyPage:
        user = user.page(1)
    return render(request, 'admindashboard/users.html', {'users': user})

def customers(request):
    c = Customer.objects.all()
    customer = Paginator(c, 1)
    page_num = request.GET.get('page', 1)
    try:
        customer = customer.page(page_num)
    except EmptyPage:
        customer = customer.page(1)
    return render(request, 'admindashboard/customers.html', {'customers': customer})

def category(request):
    c = Category.objects.all()
    categories = Paginator(c, 1)
    page_num = request.GET.get('page', 1)
    try:
        categories = categories.page(page_num)
    except EmptyPage:
        categories = categories.page(1)
    return render(request, 'admindashboard/category.html', {'category': categories})
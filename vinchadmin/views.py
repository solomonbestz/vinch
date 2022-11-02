from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage
from account.models import NewUser
from store.models import *



def dashboard(request):
    return render(request, 'admindashboard/dashboard.html')

def users(request):
    if request.user.is_authenticated:
        u = NewUser.objects.all()
        user = Paginator(u, 10)
        page_num = request.GET.get('page', 1)

        try:
            user = user.page(page_num)
        except EmptyPage:
            user = user.page(1)
    else:
        redirect('authentication')
    return render(request, 'admindashboard/users.html', {'users': user})

def customers(request):
    if request.user.is_authenticated:

        c = Customer.objects.all()
        customer = Paginator(c, 10)
        page_num = request.GET.get('page', 1)
        try:
            customer = customer.page(page_num)
        except EmptyPage:
            customer = customer.page(1)
    else:
        return redirect('authentication')
    return render(request, 'admindashboard/customers.html', {'customers': customer})

def category(request):
    if request.user.is_authenticated:
        c = Category.objects.all()
        categories = Paginator(c, 10)
        page_num = request.GET.get('page', 1)
        try:
            categories = categories.page(page_num)
        except EmptyPage:
            categories = categories.page(1)
    else:
        return redirect('authentication')
    return render(request, 'admindashboard/category.html', {'category': categories})

def products(request):
    if request.user.is_authenticated:
        prod = Product.objects.all()
    else:
        return redirect('authentication')
    return render(request, 'admindashboard/all_products.html', {'product': prod})

def orders(request):
    if request.user.is_authenticated:
        o = Order.objects.all()
        order = Paginator(o, 10)
        page_num = request.GET.get('page', 1)
        try:
            order = order.page(page_num)
        except EmptyPage:
            order = order.page(1)
    else:
        return redirect('authentication')
    return render(request, 'admindashboard/all_orders.html', {'order': order})
from unicodedata import category
from django.shortcuts import render
from .models import *

# Store function
def store(request):
    vinch_products = Product.objects.filter(category_id= 2)
    context = {'vinch_products': vinch_products}
    return render(request, 'store/store.html', context)

#Cart function
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


#Checkout function
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

#Product View Function
def productview(request):
    context = {}
    return render(request, 'store/productview.html', context)


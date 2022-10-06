from django.shortcuts import render
from django.http import JsonResponse

from .models import *

# Store function
def store(request):
    local_market = Product.objects.filter(category_id= 1)
    vinch_products = Product.objects.filter(category_id= 2)
    context = {'vinch_products': vinch_products}
    return render(request, 'store/store.html', context)

#Cart function
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


#Checkout function
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)

#Product View Function
def productview(request):
    context = {}
    return render(request, 'store/productview.html', context)

def updateItem(request):
    return JsonResponse('Item was added', safe=False)


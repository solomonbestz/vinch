
from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
import datetime

from .models import *

# Store function
def store(request):
    local_market = Product.objects.filter(category_id= 1)
    vinch_products = Product.objects.filter(category_id= 2)
    context = {'vinch_products': vinch_products}
    return render(request, 'store/store.html', context)

#Cart function
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    print(items)
    if not items:
        return redirect('store')
    return render(request, 'store/cart.html')


#Checkout function
def checkout(request):
    if request.user.is_authenticated:
        display = True
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        try:
            shipping = ShippingAddress.objects.filter(customer=customer)
            if shipping.exists():
                display = False
        except:
            pass
    else:
        return redirect('authentication')

    context = {'items': items, 'order': order, 'display': display}
    return render(request, 'store/checkout.html', context)

#Product View Function
def productview(request):
    return render(request, 'store/productview.html')

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']


    print('Action:', action)
    print('Product:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
        
    
def processOrder(request):  
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
        total = int(data['shipping']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                country = data['shipping']['country'],
                zipcode = data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in')
    return JsonResponse('Payment Submitted...', safe=False)



from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
import json
import datetime

from .models import *

# Store function
def store(request):
    category_view_1 = Category.objects.filter(id= 2)
    category_view_2  = Category.objects.filter(id= 3)
    vinch_foods =Product.objects.filter(category_id= 1)
    vinch_foodstuffs = Product.objects.filter(category_id= 2)
    vinch_nuts = Product.objects.filter(category_id= 3)

    context = {'vinch_foods': vinch_foods, 'vinch_foodstuffs': vinch_foodstuffs, 'vinch_nuts': vinch_nuts, 'category_view_1': category_view_1, 'category_view_2': category_view_2}
    return render(request, 'store/store.html', context)

#Cart function
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        if not items:
            return redirect('store:home')
    else:
        pass
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

def categoryview(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product_category = Product.objects.filter(category=category)
    return render(request, 'store/categoryview.html', {'product_category': product_category})


#Product View Function
def productview(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/productview.html', {'product': product})

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


def neworderprocess(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
        total = int(data['itemtotal']['total'])

        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        
        order.save()

    return JsonResponse('New Order Total', safe=False)
    
def processOrder(request):  
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
        user = NewUser.objects.get(customer=customer)
        total = int(data['shipping']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                first_name = user.first_name,
                last_name = user.last_name,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                country = data['shipping']['country'],
                zipcode = data['shipping']['zipcode'],
            )
            
    else:
        print('User is not logged in')
    return JsonResponse('Payment Submitted...', safe=False)





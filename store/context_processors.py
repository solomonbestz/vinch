from .models import Order, OrderItem, Product
import json


def total_cart_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        if order:
            orderitems = OrderItem.objects.filter(order=order)
            qty = sum([item.quantity for item in orderitems])
            cart_total = sum([item.get_total for item in orderitems])
        else:
            qty = 0
            cart_total = 0
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        qty = 0
        cart_total = 0
        items = []
        for i in cart:
            qty += cart[i]['quantity']
            product = Product.objects.get(id=i)
            cart_total += (product.price * cart[i]['quantity'])

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image': product.image,
                },
                'quantity': cart[i]['quantity'],
                'get_total': (product.price * cart[i]['quantity'])
            }
            items.append(item)
            print(item['product']['id'])

    return {'qty': qty, 'cart_total': cart_total, 'items': items}

# def get_cart_total(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order = Order.objects.get(customer=customer, complete=False)

#         orderitems = order.orderitem_set.all()
#         cart_total = sum([item.get_total for item in orderitems])
#     return {'cart_total': cart_total}

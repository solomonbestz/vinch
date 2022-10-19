from .models import Order, OrderItem, Product
import json


def total_cart_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
        items = order.order_items.all()
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
            try:
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
            except:
                pass

    return {'qty': qty, 'cart_total': cart_total, 'items': items}



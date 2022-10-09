from .models import Order, OrderItem


def total_cart_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer

        order = Order.objects.get(customer=customer)

        if order:
            orderitems = OrderItem.objects.filter(order=order)
            qty = sum([item.quantity for item in orderitems])
            cart_total = sum([item.get_total for item in orderitems])
        else:
            qty = 0
    else:
        cart_total = 0
        qty = 0
    return {'qty': qty, 'cart_total': cart_total}

# def get_cart_total(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order = Order.objects.get(customer=customer, complete=False)

#         orderitems = order.orderitem_set.all()
#         cart_total = sum([item.get_total for item in orderitems])
#     return {'cart_total': cart_total}

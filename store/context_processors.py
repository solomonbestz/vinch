from .models import Order, OrderItem


def total_cart_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer

        order = Order.objects.get(customer=customer, complete=False)

        if order:
            orderitems = OrderItem.objects.filter(order=order)
            qty = sum([item.quantity for item in orderitems])

        else:
            qty = 0
    else:
        qty = 0
    return {'qty': qty}
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage
from account.models import NewUser
from store.models import *



def dashboard(request):
    if request.user.is_authenticated:
        user = NewUser.objects.filter(is_active=True).count()
        customer = Customer.objects.all().count()
        order = Order.objects.filter(complete = True).count()
        product = Product.objects.all().count()
        context = {
            'user': user,
            'customer': customer,
            'order': order,
            'product': product
        }
    return render(request, 'admindashboard/dashboard.html', context)

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

def add_product(request):
    if request.user.is_authenticated:
        category = Category.objects.all()
        if request.method == "POST":
            name = request.POST.get("name")
            cat = request.POST.get("categ")
            slug = request.POST.get("slug")
            description = request.POST.get("description")
            in_stock = request.POST.get("instock")
            price = request.POST.get("price")
            image = request.FILES["image"]

            cate = Category.objects.get(name=cat)


            Product.objects.create(name = name, category = cate, slug = slug, description = description, in_stock = True, price = price, image = image)
            
            return redirect('dashboard')
    return render(request, 'admindashboard/add_product.html', {'category': category})

def add_category(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            slug = request.POST.get("slug")

            Category.objects.create(name=name, slug=slug)
            return redirect('dashboard')
    return render(request, 'admindashboard/add_category.html')
    
def orders(request):
    if request.user.is_authenticated:
        o = Order.objects.all()
        order = Paginator(o, 5)
        page_num = request.GET.get('page', 1)
        try:
            order = order.page(page_num)
        except EmptyPage:
            order = order.page(1)
    else:
        return redirect('authentication')
    return render(request, 'admindashboard/all_orders.html', {'order': order})


def view_order(request, id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, id=id)
        order_item = order.orderitem_set.all()

    return render(request, "admindashboard/view_order.html", {'order_item': order_item})

def edit_order(request, id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, id=id)
        if request.method == "POST":
            order_status = request.POST.get('status')
            transaction_id = request.POST.get('transaction_id')

            order.order_status = order_status
            order.transaction_id = transaction_id

            order.save()
            return redirect('dashboard')

    return render(request, "admindashboard/edit_order.html", {'order': order})


def view_customer(request, id):
    if request.user.is_authenticated:
        customer = get_object_or_404(NewUser, id=id)
        customer_user = get_object_or_404(Customer, id=id)
        try:
            shipping = ShippingAddress.objects.get(customer = customer_user)
        except:
            shipping ={}

    return render(request, 'admindashboard/view_customer.html', {'customer': customer, 'shipping': shipping})


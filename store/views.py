from django.shortcuts import render

# Store function
def store(request):
    context = {}
    return render(request, 'store/store.html', context)

#Cart function
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


#Checkout function
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


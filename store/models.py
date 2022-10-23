from django.db import models
from account.models import NewUser

# Create your models here.
# Create your models here. 
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name 

class Customer(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.user)


class Product(models.Model):
    name = models.CharField(max_length=200)  
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    order_status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0][0], null=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = True
        return shipping
        
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
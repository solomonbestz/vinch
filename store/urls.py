from django.urls import path

from . import views

urlpatterns = [
   path('', views.store, name="store"),
   path('cart/', views.cart, name="cart"),
   path('checkout/', views.checkout, name="checkout"),
   path('productview/', views.productview, name="productview"),

   # Url paths for json data
   path('update_item/', views.updateItem, name="update_item"), 
   path('process_order/', views.processOrder, name="proces_order"),
] 

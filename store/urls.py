from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
   path('', views.store, name="home"),
   path('cart/', views.cart, name="cart"),
   path('checkout/', views.checkout, name="checkout"),
   path('product/<slug:slug>/', views.productview, name='product_detail'),
   path('category/<slug:category_slug>/', views.categoryview, name='category_detail'),

   # Url paths for json data
   path('update_item/', views.updateItem, name="update_item"), 
   path('process_order/', views.processOrder, name="proces_order"),
   path('newprocess_order/', views.neworderprocess, name="newprocess_order"),
] 

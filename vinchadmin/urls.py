from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('users/', views.users, name="users"),
    path('customers/', views.customers, name="customers"),
    path('category/', views.category, name="category"),
    path('products/', views.products, name="all_product"),
    path('product_orders/', views.orders, name="orders"),
    path('products/add/', views.add_product, name="add_product"),
    path('categories/add/', views.add_category, name="add_category"),
    path('view_order/<int:id>/', views.view_order, name="view_order"),
    path('edit_order/<int:id>/', views.edit_order, name="edit_order"),
    path('view_customer/<int:id>/', views.view_customer, name="view_customer"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('users/', views.users, name="users"),
    path('customers/', views.customers, name="customers"),
    path('category/', views.category, name="category"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.authentication, name='authentication'),
    path("signout/", views.signout, name="signout"),
    path("account/", views.my_account, name="my_account"),
    path("orders/", views.my_orders, name="my_order"),

    # Verify Account Url
    path('activate/<uidb64>/<token>/', views.ActivateAccount, name="activate"),
    # Verification 404
    path('verification_404/', views.verification_404, name="verify_404"),
]
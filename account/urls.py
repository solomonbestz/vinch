from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.authentication, name='authentication'),
    path("signout/", views.signout, name="signout"),
    path("account/", views.my_account, name="my_account"),

    # Verification 404
    path('verification_404/', views.verification_404, name="verify_404"),
]
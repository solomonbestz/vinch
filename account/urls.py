from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.authentication, name='authentication'),
    path("signout/", views.signout, name="signout"),

    # Verification 404
    path('verification_404/', views.verification_404, name="verify_404"),
]
from django.db.models.signals import post_save
from account.models import NewUser
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender=NewUser)
def create_customer(sender, instance, created, **kwargs):
    print("I created New User")

@receiver(post_save, sender=NewUser)
def save_customer(sender, instance, **kwargs):
    print("customer saved")
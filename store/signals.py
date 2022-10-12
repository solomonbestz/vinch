from django.db.models.signals import post_save
from account.models import NewUser
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender = NewUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()
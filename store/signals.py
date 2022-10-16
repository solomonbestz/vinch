from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import NewUser, Phone
from .models import Customer

@receiver(post_save, sender=NewUser)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.middle_name, email=instance.email)
        Phone.objects.create(user=instance, phone_number=instance.phone_number)


@receiver(post_save, sender=NewUser)
def update_customer(sender, instance, created, **kwargs):
    if created == False:
        instance.customer.save()
        instance.phone.save()



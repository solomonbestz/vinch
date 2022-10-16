import imp
import django
from django.core.validators import RegexValidator
from django.db import models
from django.dispatch import Signal
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


user_created = Signal()

# Custom Account Manager class inherenting from baseuser
class CustomAccountManager(BaseUserManager):
    # Method to create new user
    def create_user(self, email, password=None, **other_fields):
        other_fields.get("first_name")
        other_fields.get("last_name")
        other_fields.get("middle_name")
        other_fields.get("gender")
        other_fields.get("phone_number")
        other_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **other_fields)

    # Method to create super staff
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("SuperUser must be a staff")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("While creating a superuser, it must be assigned true")

        return self._create_user(email, password, **other_fields)

    #Custom method to create a user
    def _create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


# New Account user class
class NewUser(AbstractBaseUser, PermissionsMixin):

    STATUS = (
        ('M', 'M'),
        ('F', 'F'),
    )

    email = models.EmailField(_("Email Adress"), unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=STATUS, null=True)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    joined_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name', 'gender']

    def __str__(self):
        return self.last_name

    # def send_user(self):
    #     user_created.send(sender=self.__class__)

class Phone(models.Model):
    user = models.OneToOneField(NewUser, blank=True, on_delete=models.CASCADE, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+234 or +(your country code)'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return str(self.user)
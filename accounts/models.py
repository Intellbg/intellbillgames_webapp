from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    phone = PhoneNumberField()


class User(AbstractUser):
    first_name = None
    last_name = None
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name="customer", null=True
    )

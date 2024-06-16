from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    first_name = None
    last_name = None



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = AbstractUser.first_name
    last_name = AbstractUser.last_name
    document_number = models.CharField(max_length=20)
    phone = PhoneNumberField()

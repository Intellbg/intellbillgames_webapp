from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    phone = PhoneNumberField(required=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
    
    @transaction.atomic
    def save(self):
        user = User.objects.create(
            username=self.cleaned_data["email"],
            email=self.cleaned_data["email"],
        )
        user.set_password(self.cleaned_data["password1"])
        customer = Customer.objects.create(
            last_name=self.cleaned_data["last_name"],
            first_name=self.cleaned_data["first_name"],
            phone=self.cleaned_data["phone"],
        )
        user.customer = customer
        user.save()
        return user

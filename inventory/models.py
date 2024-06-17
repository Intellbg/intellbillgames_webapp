from django.db import models
from accounts.models import Customer


class BaseProduct(models.Model):
    SUPPLIES = "S"
    SINGLES = "SC"
    OTHER = "O"
    SEALED_PRODUCT = "SP"

    CATEGORY_CHOICES = [
        (SUPPLIES, "Supplies"),
        (SINGLES, "Singles"),
        (OTHER, "Other"),
        (SEALED_PRODUCT, "Sealed product"),
    ]

    name = models.CharField(max_length=200)
    in_store = models.IntegerField()
    in_storage = models.IntegerField()
    in_collection = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    imagen = models.ImageField(upload_to="products/", null=True)


class Product(BaseProduct):
    detail = models.TextField()





class Order(models.Model):
    date = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    products = models.ManyToManyField(BaseProduct, through="OrderDetail")
    status = models.CharField(max_length=2)

class OrderDetail(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
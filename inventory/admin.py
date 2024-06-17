from django.contrib import admin
from inventory.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
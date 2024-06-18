from django.contrib import admin
from inventory.models import Product, Order, OrderDetail

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass
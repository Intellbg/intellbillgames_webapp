from django.shortcuts import redirect, render, get_object_or_404
from .models import BaseProduct
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderDetail


def shop(request):
    product_list = BaseProduct.objects.all()
    paginator = Paginator(product_list, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "inventory/shop.html", {"page_obj": page_obj})


@login_required
def order_detail(request):
    order, created = Order.objects.get_or_create(customer=request.user.customer)
    return render(request, "inventory/order_detail.html", {"order": order})


@login_required
def add_to_order(request, product_id):
    product = get_object_or_404(BaseProduct, id=product_id)
    order, created = Order.objects.get_or_create(customer=request.user.customer)
    order_item, created = OrderDetail.objects.get_or_create(
        order=order, product=product, defaults={"quantity":1}
    )

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect("order_detail")


@login_required
def remove_from_order(request, product_id):
    product = get_object_or_404(BaseProduct, id=product_id)
    order = get_object_or_404(Order, customer=request.user.customer)
    order_item = get_object_or_404(OrderDetail, order=order, product=product)
    order_item.delete()
    return redirect("order_detail")

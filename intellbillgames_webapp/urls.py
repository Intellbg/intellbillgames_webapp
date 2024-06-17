from django.contrib import admin
from django.urls import path, include
import accounts.views as v
from intellbillgames_webapp import settings
import inventory.views as i
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", v.index, name="index"),
    path("login", v.account_login, name="login"),
    path("logout", v.account_logout, name="logout"),
    path("signup", v.signup, name="signup"),
    path("shop", i.shop, name="shop"),
    path("order/", i.order_detail, name="order_detail"),
    path("add_to_order/<int:product_id>/", i.add_to_order, name="add_to_order"),
    path(
        "remove_from_order/<int:product_id>/",
        i.remove_from_order,
        name="remove_from_order",
    ),
    path("chat/", include("chat.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Customer
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "Intell Bill Games"
admin.site.site_title = "Intell Bill Games"


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class UserInline(admin.StackedInline):
    model = User
    fieldsets = ((None, {"fields": ("username", "password", "email")}),)
    readonly_fields = ("password",)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = (UserInline,)

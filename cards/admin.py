from django.contrib import admin
from .models import OnePieceGameCard, Set


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    pass


@admin.register(OnePieceGameCard)
class OnePieceGameCardAdmin(admin.ModelAdmin):
    pass

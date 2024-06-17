from django.contrib import admin
from .models import OnePieceGameCard, Set


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display=['name','code']


@admin.register(OnePieceGameCard)
class OnePieceGameCardAdmin(admin.ModelAdmin):
    list_display=['name','code']


from django.contrib import admin
from .models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'mfr', 'category', 'buy_price', 'quantity', 'sell_price')

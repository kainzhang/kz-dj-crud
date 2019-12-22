from django.contrib import admin
from .models import Vip


@admin.register(Vip)
class VipAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'phone')

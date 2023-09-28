from django.contrib import admin
from app_profile.models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'stock', 'weight', 'price', 'price', 'discount', 'delivery', 'available', 'picture' ]
    # list_editable = ['stock', 'weight', 'charge', 'price']
    list_per_page = 10
    list_filter = ['title']  # ตัวกรองรายการสินค้า
    search_fields = ['id', 'title']  # ช่องค้นหาสินค้า


# ลงทะเบียนคลาส ProductAdmin กับโมเดล 'Product'
admin.site.register(Products, ProductAdmin)

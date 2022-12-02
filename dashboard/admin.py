from django.contrib import admin
from . models import *

admin.site.site_header = "SamInventory Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
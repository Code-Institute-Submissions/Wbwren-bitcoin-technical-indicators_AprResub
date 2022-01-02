from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'description',
    )

admin.site.register(Product, ProductAdmin)
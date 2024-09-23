from django.contrib import admin
from .models import Product, Category, Order
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'image_tag']  # Display image
    search_fields = ['name', 'category__name']
    list_filter = ['category']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return ''
    image_tag.short_description = 'Image'
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer_name', 'quantity', 'order_status']
    search_fields = ['customer_name', 'product__name']
    list_filter = ['order_status']

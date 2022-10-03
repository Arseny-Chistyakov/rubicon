from django.contrib import admin

from products.models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')
    fields = ('name', 'category', 'description', 'price')
    search_fields = ('name',)
    ordering = ('-price',)

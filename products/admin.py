from django.contrib import admin

from products.models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')  # отображаемые объекты в таблице
    fields = ('name', 'category', 'description', 'price')  # кастомизация в карточке товара
    search_fields = ('name',)  # поиск по выбранному столбцу
    ordering = ('-price',)  # сортировка по умолчанию по выбранному столбцу

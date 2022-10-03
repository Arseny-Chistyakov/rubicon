from uuid import uuid4

from django.db import models


class ProductCategory(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Имя продукта')
    description = models.TextField(verbose_name='Описание продукта')
    price = models.PositiveIntegerField(default=0, verbose_name='Стоимость продукта')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество продукта')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория продукта')

    def __str__(self):
        return f' Продукт: {self.name}| Категория: {self.category.name}'

    def safe_delete_product(self):
        self.quantity = 0
        self.save()

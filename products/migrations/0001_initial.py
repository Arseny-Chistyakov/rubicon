# Generated by Django 3.2.12 on 2022-09-27 13:30

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя продукта')),
                ('description', models.TextField(verbose_name='Описание продукта')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Стоимость продукта')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество продукта')),
                ('category',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory',
                                   verbose_name='Категория продукта')),
            ],
        ),
    ]

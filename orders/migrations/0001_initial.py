# Generated by Django 3.2.12 on 2022-10-03 21:05

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Время создания заказа')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Время обновления заказа')),
                ('paid', models.DateTimeField(blank=True, null=True, verbose_name='Время оплаты заказа')),
                ('status', models.CharField(
                    choices=[('FM', 'Формируется'), ('STP', 'Отправлен в обработку'), ('PD', 'Оплачен'),
                             ('PRD', 'Обрабатывается'), ('RDY', 'Готов к выдачи'), ('CNC', 'Отмена заказа')],
                    default='FM', max_length=50, verbose_name='Состояние')),
                ('is_active', models.BooleanField(default=True, verbose_name='Выполнен ли заказ?')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество товара в заказе')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems',
                                            to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product',
                                              verbose_name='Продукты в заказе')),
            ],
        ),
    ]

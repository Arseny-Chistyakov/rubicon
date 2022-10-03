from uuid import uuid4

from django.conf import settings
from django.db import models

from products.models import Product


# TODO: полностью переделать заказы начиная от шаблона, заканчивая новым функционалом
class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCESSED = 'STP'
    PAID = 'PD'
    PROCESSED = 'PRD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'Формируется'),
        (SEND_TO_PROCESSED, 'Отправлен в обработку'),
        (PAID, 'Оплачен'),
        (PROCESSED, 'Обрабатывается'),
        (READY, 'Готов к выдачи'),
        (CANCEL, 'Отмена заказа'),
    )
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Заказчик')
    created = models.DateTimeField(auto_now=True, verbose_name='Время создания заказа')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Время обновления заказа')
    paid = models.DateTimeField(null=True, blank=True, verbose_name='Время оплаты заказа')
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=50, default=FORMING, verbose_name='Состояние')
    is_active = models.BooleanField(default=True, verbose_name='Выполнен ли заказ?')

    def __str__(self):
        return f'Текущий заказ {self.uid}'

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.get_product_cost(), items)))

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    # def get_items(self):
    #     pass

    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.save()
        self.is_active = False
        self.save()


class OrderItem(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукты в заказе')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара в заказе')

    def get_product_cost(self):
        return self.product.price * self.quantity

from uuid import uuid4

from django.db import models

from products.models import Product
from users.models import User


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Корзина для пользователя')
    # TODO: M2M for product
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукты в корзине')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество товаров в корзине')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления товара')

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        """ Отображение суммы товара с учетом количества в корзине """
        return int(self.quantity * self.product.price)

    def total_quantity(self):
        """ Общее количество товаров в корзине """
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        """ Общая сумма корзины """
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    def delete(self, *args, **kwargs):
        """
        При удалении товаров из корзины/при отмене заказа добавление товара в общее количество(возврат резерва на склад)
        """
        self.product.quantity += self.quantity
        self.save()
        super(Basket, self).delete(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     """
    #     При добавлении товаров в корзину/при оформлении заказов вычет из общего количества(резервация товара на складе)
    #     """
    #     if self.pk:
    #         item = self.get_item(self.pk)
    #         self.product.quantity -= self.quantity - item
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(Basket, self).save(*args, **kwargs)
    #
    # @staticmethod
    # def get_item(uid):
    #     return Basket.objects.get(pk=uid).quantity

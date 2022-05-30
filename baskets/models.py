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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    # отображение суммы товара с учетом количества в корзине
    def sum(self):
        return int(self.quantity * self.product.price)

    # подсчёт общего количества товаров в корзине
    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    # подсчёт общей суммы корзины
    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    # при добавлении товаров в корзину/при оформлении заказов вычет из общего количества(резервация товара на складе)
    def save(self, *args, **kwargs):
        if self.pk:
            item = self.get_item(int(self.pk))
            self.product.quantity -= self.quantity - item
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(Basket, self).save(*args, **kwargs)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity

    # при удалении товаров из корзины/при отмене заказа добавление товара в общее количество(возврат резерва на склад)
    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.save()
        super(Basket, self).delete(*args, **kwargs)

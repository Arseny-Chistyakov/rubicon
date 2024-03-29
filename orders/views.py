from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from baskets.models import Basket
from orders.forms import OrderItemsForm
from orders.models import Order, OrderItem


class OrderList(ListView):
    template_name = 'orders/order_list.html'
    model = Order
    title = 'GeekShop | Список заказов'


class OrderCreate(CreateView):
    template_name = 'orders/orders_create.html'
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'GeekShop | Создание заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data()
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_item = Basket.objects.filter(user=self.request.user)
            if basket_item:
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=basket_item.count())
                formset = OrderFormSet()

                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[num].product
                    form.initial['quantity'] = basket_item[num].quantity
                    form.initial['price'] = basket_item[num].product.price
                basket_item.delete()
            else:
                formset = OrderFormSet()

        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrderCreate, self).form_valid(form)


class OrderUpdate(UpdateView):
    template_name = 'orders/orders_update.html'
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'GeekShop | Создание заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderUpdate, self).get_context_data()
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:

            formset = OrderFormSet(instance=self.object)
            for num, form in enumerate(formset.forms):
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price

        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrderUpdate, self).form_valid(form)


class OrderRead(DetailView):
    template_name = 'orders/orders_read.html'
    model = Order
    title = 'GeekShop | Просмотр заказа'


class OrderDelete(DeleteView):
    template_name = 'orders/orders_delete.html'
    model = Order
    success_url = reverse_lazy('orders:list')
    title = 'GeekShop | Удаление заказа'


def order_forming_complete(request, pk):
    order = Order.objects.get(uid=pk)
    order.status = Order.SEND_TO_PROCESSED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))

# # резервация/отмена резерва через сигналы
# @receiver(pre_save, sender=OrderItem)
# @receiver(pre_save, sender=Basket)
# def product_quantity_update_save(sender, instance, **kwargs):
#     if instance.pk:
#         item = instance.get_item(int(instance.pk))
#         instance.product.quantity -= instance.quantity - item
#     else:
#         instance.product.quantity -= instance.quantity
#     instance.product.save()
#
#
# @receiver(pre_delete, sender=OrderItem)
# @receiver(pre_delete, sender=Basket)
# def product_quantity_update_delete(sender, instance, **kwargs):
#     instance.product.quantity += instance.quantity
#     instance.save()

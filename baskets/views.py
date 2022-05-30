from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string

from baskets.models import Basket
from products.models import Product


@login_required
def basket_add(request, product_id):
    user_select = request.user
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=user_select, product=product)

    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=user_select, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # возвращает пользователя на страницу,
    # где было произведено действие


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/basket.html', context)
        return JsonResponse({'result': result})
    else:
        return HttpResponseBadRequest('Invalid request')


# @login_required
# def basket_add(request, product_id):
#     if request.is_ajax():
#         user_select = request.user
#         product = Product.objects.get(id=product_id)
#         baskets = Basket.objects.filter(user=user_select, product=product)
#         if baskets:
#             basket = baskets.first()
#             basket.quantity += 1
#             basket.save()
#         else:
#             Basket.objects.create(user=user_select, product=product, quantity=1)
#         products = Product.objects.all()
#         context = {'products': products}
#         result = render_to_string('products/product.html', context)
#         return JsonResponse({'result': result})
#     else:
#         return HttpResponseBadRequest('Invalid request')

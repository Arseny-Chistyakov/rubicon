from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string

from baskets.models import Basket
from products.models import Product


@login_required
def basket_add(request, product_id):
    if request.is_ajax():
        user_select = request.user
        product = Product.objects.get(pk=product_id)
        baskets = Basket.objects.filter(user=user_select, product=product)
        if baskets:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=user_select, product=product, quantity=1)
        return HttpResponse(status=200)
    else:
        return HttpResponseBadRequest('Invalid request')


@login_required
# TODO: added button delete all product in basket
def basket_remove(request, basket_id):
    try:
        basket = Basket.objects.get(pk=basket_id)
        basket.delete()
    except:
        return {'baskets': []}
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(pk=id)
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

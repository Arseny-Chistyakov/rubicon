from django.shortcuts import render

from .models import Product, ProductCategory


def index(request):
    return render(request, 'products/product.html', context={'title': 'Услуги'})


def filter_category_products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context = {
        'title': 'Услуги',
        'categories': ProductCategory.objects.all(),
        'products': products,
    }
    return render(request, 'products/product.html', context)

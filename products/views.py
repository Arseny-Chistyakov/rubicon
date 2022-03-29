from django.shortcuts import render

from products.models import ProductCategory, Product, export_to_sqlite


def index(request):
    context = {'title': 'Рубикон - Продукты'}
    return render(request, 'products/product.html', context=context)


def products(request, category_id=None):
    if Product.objects.count() == 0:
        export_to_sqlite()
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context = {
        'title': 'Рубикон - Продукты',
        'categories': ProductCategory.objects.all(),
        'products': products,
    }
    return render(request, 'products/product.html', context)

from django.urls import path

from products.views import filter_category_products

app_name = 'products'

urlpatterns = [
    path('', filter_category_products, name='index'),
    path('<uuid:category_id>/', filter_category_products, name='category'),
]

from django.urls import path

from baskets.views import basket_add, basket_remove, basket_edit

app_name = 'basket'

urlpatterns = [
    path('basket_add/<uuid:product_id>/', basket_add, name='basket_add'),
    path('basket_remove/<uuid:basket_id>/', basket_remove, name='basket_remove'),
    path('basket_edit/<uuid:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]

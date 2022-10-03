from django.urls import path

from orders.views import OrderUpdate, OrderList, OrderRead, OrderCreate, OrderDelete, order_forming_complete

app_name = 'orders'
urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('update/<uuid:pk>/', OrderUpdate.as_view(), name='update'),
    path('read/<uuid:pk>/', OrderRead.as_view(), name='read'),
    path('delete/<uuid:pk>/', OrderDelete.as_view(), name='delete'),
    path('forming_complete/<uuid:pk>/', order_forming_complete, name='forming_complete'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blogs.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('admins-special/', include('admins.urls', namespace='admins_special')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('baskets/', include('baskets.urls', namespace='baskets')),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

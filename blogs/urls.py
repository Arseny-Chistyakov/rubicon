from django.urls import path

from blogs.views import blogs

app_name = 'blogs'

urlpatterns = [
    path('', blogs, name='index'),
]

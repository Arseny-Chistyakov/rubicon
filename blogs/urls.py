from django.urls import path

from blogs.views import blogs, post_detail

app_name = 'blogs'

urlpatterns = [
    path('', blogs, name='index'),
    path('page/<int:page>/', blogs, name='page'),
    path('post_detail/<slug:post_slug>/', post_detail, name='post_detail'),
]

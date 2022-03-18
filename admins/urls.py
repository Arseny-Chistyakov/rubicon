from django.urls import path

from admins.views import index, UserAdminListView, UserAdminCreateView, UserAdminUpdateView, UserAdminDeleteView, \
    PostAdminListView, PostAdminCreateView, PostAdminUpdateView, PostAdminDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),

    path('users/', UserAdminListView.as_view(), name='admin_users'),
    path('users-create/', UserAdminCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserAdminUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserAdminDeleteView.as_view(), name='admin_users_delete'),

    path('posts/', PostAdminListView.as_view(), name='admin_posts'),
    path('posts-create/', PostAdminCreateView.as_view(), name='admin_posts_create'),
    path('posts-update/<int:pk>/', PostAdminUpdateView.as_view(), name='admin_posts_update'),
    path('posts-delete/<int:pk>/', PostAdminDeleteView.as_view(), name='admin_posts_delete'),
]

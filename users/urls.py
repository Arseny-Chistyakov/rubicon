from django.urls import path

from users.views import UserLoginFormView, UserRegisterFormView, UserLogoutView, UserProfileFormView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginFormView.as_view(), name='login'),
    path('registration/', UserRegisterFormView.as_view(), name='registration'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileFormView.as_view(), name='profile'),
]

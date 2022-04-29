from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, FormView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User


class UserRegisterFormView(FormView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    title = 'GeekShop - Регистрация'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Register has been finished')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.error(request, form.errors)
        context = {'form': form}
        return render(request, self.template_name, context)


class UserLoginFormView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'GeekShop - Авторизация'


class UserLogoutView(LogoutView):
    template_name = 'blogs/index.html'


class UserProfileFormView(UpdateView):
    title = 'GeekShop - Профиль'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.pk)

    def form_valid(self, form):
        messages.success(self.request, 'Data has been saved')
        super(UserProfileFormView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

#
# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             messages.success(request, 'Congratulation! Success registration ')
#             form.save()
#             return HttpResponseRedirect(reverse('users:login'))
#         else:
#             print(form.errors)
#     else:
#         form = UserRegistrationForm()
#     context = {'title': 'GeekShop - Регистрация', 'form': form}
#     return render(request, 'users/registration.html', context=context)

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 print(form.errors)
#     else:
#         form = UserLoginForm()
#     context = {'title': 'GeekShop - Авторизация', 'form': form}
#     return render(request, 'users/login.html', context=context)

# @login_required
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             messages.success(request, 'Data has been saved ')
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=user)
#     context = {
#         'title': 'GeekShop - Профиль',
#         'form': form,
#     }
#     return render(request, 'users/profile.html', context=context)

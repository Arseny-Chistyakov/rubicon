from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
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
            user = form.save()
            if self.send_verify_link(user):
                messages.success(self.request, 'Для завершения регистрации пройдите верификацию по почте!')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.error(request, form.errors)
        else:
            messages.error(request, form.errors)
        context = {'form': form}
        return render(request, self.template_name, context)

    def send_verify_link(self, user):
        verify_link = reverse('users:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылки'
        # {settings.DOMAIN_NAME} убрал настройку чтобы в начале ссылки для активации не было mail.ru пока что
        message = f'Для подтверждения учетной записи {user.username} на портале \n {verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activate_key):
        user = User.objects.get(email=email)
        if user and user.activation_key == activate_key and not user.is_activation_key_expires():
            user.activation_key = ''
            user.activation_key_expires = None
            user.is_active = True
            user.save()
            auth.login(self, user)
        return render(self, 'users/verification.html')


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
        messages.success(self.request, 'Данные успешно сохранены')
        super(UserProfileFormView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    # добавлено в контекстный процессор
    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileFormView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context
#
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
#         'baskets': Basket.objects.filter(user=user),
#     }
#     return render(request, 'users/profile.html', context)

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

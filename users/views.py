import jwt
import random
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView

from users.forms import UserForm, UserRegisterForm, UserLoginForm

from users.models import User

# Create your views here.


class UserLoginView(LoginView):
    
    form_class = UserLoginForm
    template_name = 'user/login.html'


class RegisterUser(CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    extra_context = {'is_active_register': 'active'}

    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        user = form.save()        

        # Сформировать токен
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        user_id = {'user_id': user.pk}
        secret_key = user.email
        token = jwt.encode(user_id, secret_key, algorithm='HS256')
        
        # Создание ссылки
        current_site = get_current_site(self.request)
        activation_link = reverse_lazy(
            'users:activate_account', kwargs={'uidb64': uid, 'token': token})
        activation_url = f"{current_site}{activation_link}"

        # Данные для письма
        mail_subject = 'Активация аккаунта'
        massage = render_to_string('users/activation_email.html', {
            'activation_url': activation_url
        })

        # Отправка письма
        send_mail(mail_subject, massage, 'djang5111@gmail.com', [user.email])

        return super().form_valid(form)


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=int(uid))
    except User.DoesNotExist:
        return redirect('users:activation_failed')
    
    try:
        secret_key = user.email
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.InvalidTokenError:
        return redirect('users:activation_failed')
    
    if decoded_token['user_id'] == user.pk:
        user.is_active = True
        user.save()
        return redirect('users:activation_success')
    else:
        return redirect('users:activation_failed')
    
    
class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def gen_new_pass(request):

    new_password = str(random.randint(1000, 9999))
    request.user.set_password(new_password)
    request.user.save()
    send_mail('Ваш пароль изменен',
              f"Ваш пароль: {new_password}", 'djang5111@gmail.com', [request.user.email])

    return redirect('catalog:index')


class ActivationSuccess(TemplateView):
    template_name = 'users/activation_success.html'


class ActivationFailed(TemplateView):
    template_name = 'users/activation_failed.html'

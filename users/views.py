

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail

from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm

from users.models import User

# Create your views here.


class RegisterUser(CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    extra_context = {'is_active_register': 'active'}

    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        user = form.save()

        # Закодировать id пользователя
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Создание ссылки
        current_site = get_current_site(self.request)
        activation_link = reverse_lazy(
            'users:activate_account', kwargs={'uidb64': uid})
        activation_url = f"{current_site}{activation_link}"

        # Данные для письма
        mail_subject = 'Активация аккаунта'
        massage = render_to_string('users/activation_email.html', {
            'activation_url': activation_url
        })

        # Отправка письма
        send_mail(mail_subject, massage, 'djang5111@gmail.com', [user.email])

        return super().form_valid(form)


def activate_account(request, uidb64):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=int(uid))
        user.is_active = True
        user.save()
        return redirect('users:activation_success')
    except User.DoesNotExist:
        return redirect('users:activation_failed')


class ActivationSuccess(TemplateView):
    template_name = 'users/activation_success.html'


class ActivationFailed(TemplateView):
    template_name = 'users/activation_failed.html'

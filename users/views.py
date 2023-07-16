from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm

from users.models import User

# Create your views here.


class RegisterUser(CreateView):
    
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    
    extra_context = {'is_active_register': 'active'}
    
    success_url = reverse_lazy('users:login')
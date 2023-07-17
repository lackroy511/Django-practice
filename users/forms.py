from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name',
                  'phone_number', 'country', 'avatar')

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    
    username = None
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    
    avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='аватар')
    phone_number = models.CharField(max_length=50, verbose_name='номер телефона')
    country = models.CharField(max_length=50, verbose_name='страна')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
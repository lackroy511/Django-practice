from django.db import models

from users.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image_preview = models.ImageField(upload_to='image_preview/',
                                      null=True, blank=True)
    category = models.ForeignKey(
        "Category", verbose_name='Категория', on_delete=models.DO_NOTHING)
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания',
                                         null=True, blank=True)
    update_date = models.DateField(auto_now=True,
                                   verbose_name='дата изменения')
    user = models.ForeignKey(User, verbose_name='пользователь',
                             on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Имя: {self.name}, Цена: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')
    description = description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'Категория: {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('id',)


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.CharField(max_length=250, verbose_name='email')
    massage = models.TextField(verbose_name='сообщение')

    def __str__(self) -> str:
        return f'Имя: {self.name}, emil: {self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(
        max_length=50, verbose_name='номер версии')
    version_name = models.CharField(
        max_length=50, verbose_name='название версии')
    version_is_active = models.BooleanField()

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

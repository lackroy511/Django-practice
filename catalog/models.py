from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image_preview = models.ImageField(
        upload_to='image_preview/', null=True, blank=True)
    category = models.BigIntegerField(verbose_name='id категории')
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания', null=True, blank=True)
    update_date = models.DateField(
        auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return f'Имя: {self.name}, Цена: {self.price}'

    class Meta:
        verbose_name = 'имя'
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
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

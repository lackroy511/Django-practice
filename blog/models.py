from django.db import models

# Create your models here.

class BlogEntry(models.Model):
    header = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=180, verbose_name='слаг', null=True, blank=True)
    content = models.TextField(verbose_name='контент')
    image_preview = models.ImageField(upload_to='blog_image_preview/', null=True, blank=True, verbose_name='Превью')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', 
                                         null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.BigIntegerField(default=0, verbose_name='Количество просмотров')
    
    def __str__(self) -> str:
        return f'{self.header}, {self.creation_date}'
    
    class Meta:
        verbose_name='запись блога'
        verbose_name_plural='записи блога'
        ordering = ('-creation_date', )
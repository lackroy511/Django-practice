# Generated by Django 4.2.2 on 2023-07-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='опубликовано'),
        ),
    ]

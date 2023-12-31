# Generated by Django 4.2.2 on 2023-07-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogentry_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentry',
            options={'ordering': ('-creation_date',), 'verbose_name': 'запись блога', 'verbose_name_plural': 'записи блога'},
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='blog_image_preview/', verbose_name='Превью'),
        ),
    ]

from django.urls import path

from catalog.apps import MainConfig
from catalog.views import contacts, index, categories, orders, product

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('orders/', orders, name='orders'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')
]

from django.urls import path

from catalog.views import contacts, index, categories, orders

urlpatterns = [
    path('', index),
    path('categories/', categories),
    path('orders/', orders),
    path('contacts/', contacts),
]

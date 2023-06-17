from django.urls import path

from catalog.views import contacts, index, category, orders

urlpatterns = [
    path('', index),
    path('category/', category),
    path('orders/', orders),
    path('contacts/', contacts),
]

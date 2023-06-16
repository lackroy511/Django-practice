from django.urls import path

from catalog.views import contacts, index

urlpatterns = [
    path('', index),
    path('', contacts)
]


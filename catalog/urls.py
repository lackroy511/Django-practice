from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import MainConfig
from catalog.views import ContactCreateView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    
    path('product/<int:pk>/',ProductDetailView.as_view(), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/',
         ProductUpdateView.as_view(), name='update_product'),
    path("delete_product/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"),
    
    path('category/', CategoryListView.as_view(), name='category'),
]

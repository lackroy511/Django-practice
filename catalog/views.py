from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from catalog.models import Product, Contact
from django.core.files.storage import FileSystemStorage

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'is_active_main': 'active'
    }


class ProductDetailView(DetailView):
    model = Product


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'email', 'massage', ) 
    success_url = reverse_lazy('catalog:contact')
    extra_context = {
        'is_active_contact': 'active'
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'image_preview',)
    success_url = reverse_lazy('catalog:index')
    
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'image_preview',)
    success_url = reverse_lazy('catalog:index')
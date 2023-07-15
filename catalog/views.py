from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView


from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Version


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'is_active_main': 'active'
    }
    
    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset
    


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
    form_class = ProductForm 
    
    success_url = reverse_lazy('catalog:index')
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        
        if self.request.method == 'POST':
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        
        return context
    
    
    def form_valid(self, form):
        
        formset = self.get_context_data()['formset']
        self.object = form.save()
        
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        
        return super().form_valid(form)
    
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm 
    
    success_url = reverse_lazy('catalog:index')
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        
        if self.request.method == 'POST':
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        
        return context
    
    
    def form_valid(self, form):
        
        formset = self.get_context_data()['formset']
        self.object = form.save()
        
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        
        return super().form_valid(form)
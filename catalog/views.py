from django.core.cache import cache
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from catalog.forms import ProductForm, VersionForm, ContactForm
from catalog.mixins import OwnerCheckMixin, CacheViewMixin
from catalog.models import Product, Contact, Version, Category

from catalog.services import cache_category, filter_products_by_owner, set_active_version_for_products, \
    create_formset_for_product, save_formset_data_for_product, choose_form_for_model
from config.settings import CACHE_ENABLED


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'is_active_main': 'active'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = filter_products_by_owner(self, queryset, Product)
        set_active_version_for_products(queryset)
        
        return queryset


class ProductDetailView(CacheViewMixin, LoginRequiredMixin, PermissionRequiredMixin, OwnerCheckMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'
    login_url = reverse_lazy('users:login')


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'

    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_formset_for_product(self, context, Product, Version, VersionForm)
        
        return context

    def form_valid(self, form):
        save_formset_data_for_product(self, form)
        
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, OwnerCheckMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'

    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:index')
    
    def get_form_class(self):
        return choose_form_for_model(self)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_formset_for_product(self, context, Product, Version, VersionForm)
        
        return context

    def form_valid(self, form):
        save_formset_data_for_product(self, form)
        
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, OwnerCheckMixin, DeleteView):

    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:index')


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contact')
    extra_context = {
        'is_active_contact': 'active'
    }
    

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'is_active_categories': 'active'
    }
    
    def get_queryset(self):
        return cache_category()
        
    
    
    
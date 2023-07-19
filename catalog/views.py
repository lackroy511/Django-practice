from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from catalog.forms import ProductForm, VersionForm, ContactForm, ProductForModeratorForm, \
    ProductForAdminForm
from catalog.mixins import OwnerCheckMixin
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

        if self.request.user.is_staff:
            pass
        elif not self.request.user.is_authenticated:
            queryset = Product.objects.none
        elif self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        try:
            for product in queryset:
                version = product.version_set.all().filter(version_is_active=True).first()
                product.version = version
        except TypeError:
            pass

        return queryset


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, OwnerCheckMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'
    login_url = reverse_lazy('users:login')


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contact')
    extra_context = {
        'is_active_contact': 'active'
    }


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'

    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context['formset'] = ProductFormset(
                self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)

        return context

    def form_valid(self, form):

        form.instance.user = self.request.user  # Добавил текущего юзера в продукт

        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, OwnerCheckMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'

    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:index')

    def get_form_class(self):

        if self.request.user.is_staff:
            return ProductForModeratorForm
        if self.request.user.is_superuser:
            return ProductForAdminForm

        return ProductForm

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1)

        if not self.request.user.is_staff:
            if self.request.method == 'POST':
                context['formset'] = ProductFormset(
                    self.request.POST, instance=self.object)
            else:
                context['formset'] = ProductFormset(instance=self.object)

        return context

    def form_valid(self, form):

        try:
            formset = self.get_context_data()['formset']
            self.object = form.save()

            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        except KeyError:
            pass

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, OwnerCheckMixin, DeleteView):

    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:index')

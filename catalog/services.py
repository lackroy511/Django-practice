from django.core.cache import cache
from django.forms import inlineformset_factory
from catalog.models import Category


from catalog.forms import ProductForAdminForm, ProductForModeratorForm, ProductForm
from config.settings import CACHE_ENABLED

def cache_category() -> object:
    if CACHE_ENABLED:
        key = 'category_list'
        queryset = cache.get(key)
        if queryset is None:
            queryset = Category.objects.all()
            cache.set(key, queryset, 60)
    else:
        queryset = Category.objects.all()
    return queryset

def filter_products_by_owner(self, queryset: object, Product: object) -> object:

    if self.request.user.groups.filter(name='Moderator').exists():
        pass
    elif not self.request.user.is_authenticated:
        queryset = Product.objects.none
    elif self.request.user.is_authenticated:
        queryset = queryset.filter(user=self.request.user)

    return queryset


def set_active_version_for_products(queryset: object) -> None:
    try:
        for product in queryset:
            version = product.version_set.all().filter(version_is_active=True).first()
            product.version = version
    except TypeError:
        pass


def create_formset_for_product(self, context: dict, Product: object, Version: object, VersionForm: object) -> dict:
    
    ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1)

    if not self.request.user.groups.filter(name='Moderator').exists():
        if self.request.method == 'POST':
            context['formset'] = ProductFormset(
                self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)

    return context

def save_formset_data_for_product(self, form) -> None:
    try:
        form.instance.user = self.request.user  # Добавил текущего юзера в продукт
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
    except KeyError:
        pass
    

def choose_form_for_model(self) -> object:
    if self.request.user.is_superuser:
        return ProductForAdminForm
    if self.request.user.groups.filter(name='Moderator').exists():
        return ProductForModeratorForm

    return ProductForm
    


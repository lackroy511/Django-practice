from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class OwnerCheckMixin:
    def dispatch(self, request, *args, **kwargs):

        object = self.get_object()
        if object.user != self.request.user and not self.request.user.groups.filter(name='Moderator').exists() \
                                            and not self.request.user.is_superuser:
                                            
            return redirect('catalog:index')

        return super().dispatch(request, *args, **kwargs)


class StylesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'version_is_active':
                continue
            if field_name == 'is_published':
                continue
            field.widget.attrs['class'] = 'form-control'


class CacheViewMixin:
    @method_decorator(cache_page(30))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

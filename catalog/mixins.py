from django.shortcuts import redirect


class OwnerCheckMixin:
    
    def dispatch(self, request, *args, **kwargs):

        object = self.get_object()
        if object.user != self.request.user and not self.request.user.is_staff \
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

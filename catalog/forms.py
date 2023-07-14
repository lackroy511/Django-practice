from typing import Any, Dict
from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    forbidden_words = 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар'

    class Meta:
        model = Product
        fields = ('name', 'description',
                  'image_preview', 'category', 'price', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'version_is_active':
                continue
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        data: str = self.cleaned_data['name']

        if data.lower() in self.forbidden_words:
            raise forms.ValidationError(
                "Название или описание содержит запрещенные слова.")


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'version_is_active':
                continue
            field.widget.attrs['class'] = 'form-control'

from typing import Any, Dict
from django import forms
from catalog.mixins import StylesMixin

from catalog.models import Product, Version, Contact


class ProductForm(StylesMixin, forms.ModelForm):

    forbidden_words = 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар'

    class Meta:
        model = Product
        fields = ('name', 'description',
                  'image_preview', 'category', 'price')

    def clean_name(self):
        data: str = self.cleaned_data['name']

        if data.lower() in self.forbidden_words:
            raise forms.ValidationError(
                "Название или описание содержит запрещенные слова.")

        return data


class ProductForAdminForm(StylesMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductForModeratorForm(StylesMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')


class VersionForm(StylesMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class ContactForm(StylesMixin, forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

from django import forms

from blog.models import BlogEntry

from catalog.mixins import StylesMixin


class BlogEntryForm(StylesMixin, forms.ModelForm):
    
    class Meta:
        model = BlogEntry
        fields = ('header', 'image_preview', 'content', 'is_published', )
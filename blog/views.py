from django.forms.models import BaseModelForm

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import BlogEntry

from django.urls import reverse, reverse_lazy

from django.shortcuts import render

from pytils.translit import slugify
# Create your views here.


class BlogEntryListView(ListView):
    model = BlogEntry
    extra_context = {
        'is_active_blog': 'active'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publish=True)
        return queryset


class BlogEntryDetailView(DetailView):
    model = BlogEntry
    
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ('header', 'image_preview', 'content', )
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form: BaseModelForm):

        if form.is_valid():
            new_entry = form.save()
            new_entry.slug = slugify(new_entry.header)
            new_entry = form.save()

        return super().form_valid(form)
    

class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ('header', 'image_preview', 'content', )
    
    def get_success_url(self) -> str:
        return reverse('blog:entry_detail', args=[self.kwargs.get('pk')])
    

class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:blog')
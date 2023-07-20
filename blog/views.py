from utils.send_mail import send_mail

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from blog.models import BlogEntry
from blog.forms import BlogEntryForm
from blog.mixins import SlugifyMixin

# Create your views here.


class BlogEntryListView(ListView):
    model = BlogEntry
    extra_context = {
        'is_active_blog': 'active'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogEntryDetailView(DetailView):
    model = BlogEntry
    slug_field = 'slug'
    
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        
        if self.object.views_count == 100:
            send_mail('Просмотры', 'Количество просмотров 10')
        
        return self.object


class BlogEntryCreateView(PermissionRequiredMixin, SlugifyMixin, CreateView):
    model = BlogEntry
    form_class = BlogEntryForm
    permission_required = 'blog.add_blogentry'
    success_url = reverse_lazy('blog:blog')


class BlogEntryUpdateView(PermissionRequiredMixin, SlugifyMixin, UpdateView):
    model = BlogEntry
    form_class = BlogEntryForm
    permission_required = 'blog.change_blogentry'
    
    def get_success_url(self) -> str:
        return reverse('blog:entry_detail', args=[self.object.slug])
    

class BlogEntryDeleteView(PermissionRequiredMixin, DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:blog')
    permission_required = 'blog.delete_blogentry'
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogEntryListView, BlogEntryDetailView, BlogEntryCreateView, BlogEntryUpdateView, BlogEntryDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('posts/', BlogEntryListView.as_view(), name='blog'),
    path('entry_detail/<slug:slug>/',BlogEntryDetailView.as_view(), name='entry_detail'),
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('entry_update/<slug:slug>/', BlogEntryUpdateView.as_view(), name='entry_update'),
    path('entry_delete/<slug:slug>/', BlogEntryDeleteView.as_view(), name='entry_delete')
]

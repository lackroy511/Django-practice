from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogEntryListView, BlogEntryDetailView, BlogEntryCreateView, BlogEntryUpdateView, BlogEntryDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogEntryListView.as_view(), name='blog'),
    path('entry_detail/<int:pk>/',BlogEntryDetailView.as_view(), name='entry_detail'),
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('entry_update/<int:pk>/', BlogEntryUpdateView.as_view(), name='entry_update'),
    path('entry_delete/<int:pk>/', BlogEntryDeleteView.as_view(), name='entry_delete')
]
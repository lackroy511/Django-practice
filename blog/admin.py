from django.contrib import admin

from blog.models import BlogEntry

# Register your models here.


admin.site.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'published_date', 'updated_date',)
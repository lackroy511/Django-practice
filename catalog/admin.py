from django.contrib import admin

from catalog.models import Category, Product, Contact

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)
    
    
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email',)
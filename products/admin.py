from django.contrib import admin
from .models import Product,File,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','description','is_enable','create_time']
    list_filter = ['is_enable','parent']
    search_fields = ['title']


class FileAdmin(admin.StackedInline):
    model = File
    fields = ['title','file','is_enable'] 
    extra = 0 
      
@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable','create_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    inlines = [FileAdmin]
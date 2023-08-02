from django.contrib import admin
from .models import Product, Repair

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ['title', 'image', 'author']
    list_display_links = ['title',]
    list_filter = ['author', 'condition']
admin.site.register(Repair)

from django.contrib import admin
from .models import Category, Omonim

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Omonim)
class OmonimAdmin(admin.ModelAdmin):
    list_display = ['word']
    search_fields = ['word']
    list_filter = ['categories']

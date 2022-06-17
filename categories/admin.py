from django.contrib import admin
from categories.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'description', 'created_at', 'updated_at')
    list_filter = ('published',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'



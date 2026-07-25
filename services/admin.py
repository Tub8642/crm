from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'base_price', 'is_active', 'duration_minutes')
    search_fields = ('name', 'description')
    list_filter = ('category', 'is_active', 'created_at')
    list_editable = ('base_price', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'category', 'description', 'base_price', 'unit')
        }),
        ('Дополнительно', {
            'fields': ('duration_minutes', 'is_active', 'created_at', 'updated_at')
        }),
    )

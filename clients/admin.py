from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'email')
        }),
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('address', 'notes', 'created_at', 'updated_at'),
        }),
    )
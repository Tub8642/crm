from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'brand', 'model', 'year', 'client', 'vin', 'created_at')
    search_fields = ('licence_plate', 'vin', 'brand', 'model', 'client__name', 'client__phone')
    list_filter = ('year', 'brand', 'client')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('client', 'license_plate', 'brand', 'model', 'year')
        }),
        ('Детали', {
            'classes': ('collapse',),
            'fields': ('vin', 'mileage') 
        }),
        ('Системные данные', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

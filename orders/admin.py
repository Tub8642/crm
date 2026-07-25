from django.contrib import admin
from .models import Order, OrderService

class OrderServiceInline(admin.TabularInline):
    model = OrderService
    extra = 1
    fields = ('service', 'quantity', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'client', 'car', 'status', 
        'total_price', 'date_received', 'date_due'
    )
    search_fields = (
        'client__name', 'client__phone', 
        'car__license_plate', 'car__vin'
    )
    list_filter = ('status', 'date_received', 'date_due')
    readonly_fields = ('date_received', 'created_at', 'updated_at', 'total_price')
    inlines = [OrderServiceInline]
    fieldsets = (
        ('Основное', {
            'fields': ('client', 'car', 'status')
        }),
        ('Даты', {
            'fields': ('date_received', 'date_due', 'date_completed')
        }),
        ('Финансы', {
            'fields': ('total_price',)
        }),
        ('Дополнительно', {
            'fields': ('notes', 'created_at', 'updated_at')
        }),
    )

@admin.register(OrderService)
class OrderServiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'service', 'quantity', 'price')
    search_fields = ('order__id', 'service__name')
    list_filter = ('order__status', 'service__category')
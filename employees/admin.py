from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone', 'salary_type', 'salary_amount', 'is_active')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('position', 'salary_type', 'is_active', 'hire_date')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'position', 'phone', 'email', 'hire_date')
        }),
        ('Оплата', {
            'fields': ('salary_type', 'salary_amount')
        }),
        ('Дополнительно', {
            'fields': ('is_active', 'notes', 'created_at', 'updated_at')
        }),
    )
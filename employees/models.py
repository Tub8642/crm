from django.db import models

class Employee(models.Model):
    POSITION_CHOICES = [
        ('master', 'Мастер'),
        ('manager', 'Менеджер'),
        ('admin', 'Администратор'),
        ('detailer', 'Детейлер'),
        ('other', 'Другое'),
    ]

    SALARY_TYPE_CHOICES = [
        ('fixed', 'Фиксированная'),
        ('percentage', 'Процент от выручки'),
        ('mixed', 'Оклад + процент'),
    ]

    name = models.CharField('ФИО', max_length=200, db_index=True)
    position = models.CharField('Должность', max_length=20, choices=POSITION_CHOICES, default='master')
    phone = models.CharField('Телефон', max_length=17, unique=True)
    email = models.EmailField('Email', blank=True, null=True)
    hire_date = models.DateField('Дата приёма', auto_now_add=True)
    salary_type = models.CharField('Тип оплаты', max_length=20, choices=SALARY_TYPE_CHOICES, default='fixed')
    salary_amount = models.DecimalField(
        'Оклад, руб.',
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text='сумма в рублях'
    )
    percentage_rate = models.DecimalField(
        'Процент от выручки',
        max_digits=5,
        decimal_places=2,
        default=0,
        help_text='например 30 = 30%'
    )
    is_active = models.BooleanField('Активен', default=True)
    notes = models.TextField('Примечания', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        indexes = [
            models.Index(fields=['position']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f'{self.name} ({self.get_position_display()})'
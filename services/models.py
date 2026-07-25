from django.db import models

class Service(models.Model):
    CATEGORY_CHOISES = [
        ('wash', 'Мойка'),
        ('polish', 'Полировка'),
        ('cleaning', 'Химчистка салона'),
        ('coating', 'Нанесение покрытий'),
        ('other', 'Другое'),
    ]

    name = models.CharField('Название услуги', max_length=100, db_index=True)
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOISES, default='other')
    description = models.TextField('Описание', blank=True)
    base_price = models.DecimalField('Базовая цена', max_digits=10, decimal_places=2, help_text='Цена в рублях(без скидки)')
    unit = models.CharField('Единица измерения', max_length=20, default='шт', help_text='например шт., час')
    duration_minutes = models.PositiveIntegerField('Длительность (минуты)', blank=True, null = True, help_text='Среднее время выполнения')
    is_active = models.BooleanField('Активна', default=True, help_text='Отображается в списке услуг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f'{self.name} ({self.base_price} руб.)'
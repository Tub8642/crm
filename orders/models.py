from django.db import models
from clients.models import Client
from cars.models import Car
from services.models import Service
from employees.models import Employee

class Order(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('confirmed', 'Подтверждён'),
        ('in_progress', 'В работе'),
        ('ready', 'Готов к выдаче'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменён'),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        verbose_name='Клиент',
        related_name='orders'
    )
    
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        verbose_name='Автомобиль',
        related_name='orders'
    )

    assigned_to = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,  # Если сотрудника удалят, заказ останется
        null=True,
        blank=True,
        verbose_name='Ответственный',
        related_name='orders'
    )

    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        db_index=True
    )

    date_received = models.DateTimeField(
        'Дата приёма',
        auto_now_add=True 
    )

    date_due = models.DateTimeField(
        'Плановая дата выдачи',
        blank=True,
        null=True
    )

    date_completed = models.DateTimeField(
        'Дата выполнения',
        blank=True,
        null=True
    )

    services = models.ManyToManyField(
        Service,
        through='OrderService',
        verbose_name='Услуги',
        blank=True
    )

    total_price = models.DecimalField(
        'Итоговая стоимость',
        max_digits=12,
        decimal_places=2,
        default=0
    )

    notes = models.TextField(
        'Комментарий',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_received']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['client']),
            models.Index(fields=['car']),
        ]

    def __str__(self):
        return f'Заказ #{self.id} — {self.car} ({self.client})'

class OrderService(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        verbose_name='Услуга'
    )
    quantity = models.PositiveIntegerField(
        'Количество',
        default=1
    )
    price = models.DecimalField(
        'Цена за единицу',
        max_digits=12,
        decimal_places=2,
        help_text='Цена на момент заказа'
    )

    class Meta:
        verbose_name = 'Услуга в заказе'
        verbose_name_plural = 'Услуги в заказе'

    def __str__(self):
        return f'{self.service.name} x {self.quantity} = {self.price * self.quantity} руб.'
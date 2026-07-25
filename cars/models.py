from django.db import models
from clients.models import Client

class Car(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cars', verbose_name='Владелец')
    brand = models.CharField('Марка', max_length=50, blank=True)
    model = models.CharField('Модель', max_length=50, blank=True)
    year = models.IntegerField('Год выпуска', blank=True)
    vin = models.CharField('VIN', max_length=17, unique=True, blank=True, null=True)
    license_plate = models.CharField('Госномер', max_length=10, db_index=True, blank=True, null=True)
    mileage = models.PositiveIntegerField('Пробег, км', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.brand} {self.model} ({self.licence_plate})'


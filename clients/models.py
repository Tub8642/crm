from django.db import models
from django.core.validators import RegexValidator

class Client(models.Model):
    name = models.CharField(
        'имя клиента',
        max_length=200,
        help_text='Полное имя клиента'
    )
    phone_regex = RegexValidator(
        regex=r'^\+7\d{10}$',
        message="Телефон должен быть в формате: '+79528032100'"
    )
    phone = models.CharField(
        'Телефон',
        validators=[phone_regex],
        max_length=17,
        unique=True,
        help_text='Введите номер с кодом страны'
    )
    email = models.EmailField(
        'Email',
        blank=True,
        null=True,
        help_text='Необязательно'
    )
    address = models.TextField(
        'Адрес',
        blank=True,
        help_text='Фактический адрес клиента'
    )
    created_at = models.DateTimeField(
        'Дата регистрации',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    ) 
    notes = models.TextField(
        'Примечания',
        blank=True,
        help_text='Примечания'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name} ({self.phone})'

    def get_full_info(self):
        return f'{self.name}, тел: {self.phone}, email: {self.email or "не указан"}'
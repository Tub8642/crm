from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum, F
from .models import OrderService, Order

def update_order_total(order):
    total = order.orderservice_set.aggregate(
        total=Sum(F('quantity') * F('price'))
    )['total'] or 0
    order.total_price = total
    order.save(update_fields = ['total_price'])

@receiver(post_save, sender=OrderService)
def order_service_saved(sender, instance, **kwargs):
    update_order_total(instance.order)

@receiver(post_delete, sender=OrderService)
def order_service_deleted(sender, instance, **kwargs):
    update_order_total(instance.order)
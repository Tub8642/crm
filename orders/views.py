from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Order

class OrderListView(ListView):
    model = Order
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/orders_detail.html'
    context_object_name = 'order'

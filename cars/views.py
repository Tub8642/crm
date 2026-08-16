from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car

class CarsListView(ListView):
    model = Car
    template_name = 'cars/cars_list.html'
    context_object_name = 'cars'
    ordering = ['client', '-created_at']

class CarsDetailView(DetailView):
    model = Car
    template_name = 'cars/cars_detail.html'
    context_object_name = 'car'
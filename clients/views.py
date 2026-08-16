from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Client

class ClientListView(ListView):
    model = Client
    template_name = 'clients/clients_list.html'
    context_object_name = 'clients'
    ordering = ['-created_at']

class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/clients_detail.html'
    context_object_name = 'client'

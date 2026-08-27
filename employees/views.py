from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    ordering_by = ['name']

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'
    
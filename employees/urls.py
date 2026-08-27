from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('<int:pk>', views.EmployeeDetailView.as_view(), name='detail')
]
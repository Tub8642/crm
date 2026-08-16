from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('cars/', include('cars.urls')),
    path('orders/', include('orders.urls')),
]

"""
URLs del PROYECTO: punto de organización de rutas.
Delega las rutas de la aplicación 'inicio' mediante include().
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),  # conecta con inicio/urls.py
]

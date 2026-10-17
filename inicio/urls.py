"""
URLs de la APLICACIÓN (archivo creado manualmente).
Relaciona una dirección con una vista mediante path().
"""
from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),  # http://127.0.0.1:8000/
]

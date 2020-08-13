# users/urls.py
from django.urls import path
from .views import registro



urlpatterns = [
    path('registro/', registro.as_view(), name='registro'),
]
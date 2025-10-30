# backend/apps/prestadores/mi_negocio/gestion_financiera/urls.py
from django.urls import path, include
urlpatterns = [path('', include('apps.financiero.urls'))]

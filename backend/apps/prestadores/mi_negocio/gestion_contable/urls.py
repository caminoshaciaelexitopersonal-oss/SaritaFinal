# backend/apps/prestadores/mi_negocio/gestion_contable/urls.py
from django.urls import path, include
urlpatterns = [path('', include('apps.contabilidad.urls'))]

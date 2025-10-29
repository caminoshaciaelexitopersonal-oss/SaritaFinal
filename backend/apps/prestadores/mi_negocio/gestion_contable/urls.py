# backend/apps/prestadores/mi_negocio/gestion_contable/urls.py
from django.urls import path, include

# Redirige las solicitudes bajo '.../contable/' a la app 'contabilidad'.
urlpatterns = [
    path('', include('apps.contabilidad.urls')),
]

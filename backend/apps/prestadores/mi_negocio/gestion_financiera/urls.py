# backend/apps/prestadores/mi_negocio/gestion_financiera/urls.py
from django.urls import path, include

# Redirige las solicitudes bajo '.../financiera/' a la app 'financiera'.
urlpatterns = [
    path('', include('apps.financiera.urls')),
]

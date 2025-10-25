"""
URL configuration for puerto_gaitan_turismo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("admin/", admin.site.urls),
    # La autenticación de la API es manejada por dj-rest-auth
    path('api/auth/', include('dj_rest_auth.urls')),

    # Rutas de la API de la aplicación principal
    path("api/", include("api.urls")),

    # Panel "Mi Negocio" para Prestadores
    path("api/v1/", include("apps.prestadores.urls")),
]

# Servir archivos multimedia en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for puerto_gaitan_turismo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # OpenAPI Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api/auth/', include('backend.api.auth_urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # Rutas de la API de la aplicación principal
    path("api/", include("backend.api.urls")),

    # Panel "Mi Negocio" para Prestadores
    path("api/v1/mi-negocio/", include("backend.apps.prestadores.mi_negocio.urls")),

    # Nueva API para el panel de administración de la plataforma
    path('api/admin/plataforma/', include('backend.apps.admin_plataforma.urls')),

    # APIs para la gobernanza del contenido web (Funnel y páginas públicas)
    path('api/web/', include('backend.apps.web_funnel.urls')),
 

 
    # APIs para la página de descargas
    # path('api/downloads/', include('backend.apps.downloads.urls')),
 
 
    # API para el carro de compras
    path('api/cart/', include('backend.apps.cart.urls')),

    # API para pagos
    path('api/payments/', include('backend.apps.payments.urls')),

    # API para el Agente SADI
    path('api/sadi/', include('backend.apps.sadi_agent.urls')),

    # API para el motor de agentes SARITA
    path('api/sarita/', include('backend.apps.sarita_agents.urls')),
]

# Servir archivos multimedia y la URL del admin en modo de desarrollo
if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

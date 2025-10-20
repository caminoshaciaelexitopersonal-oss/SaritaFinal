"""
URL configuration for puerto_gaitan_turismo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # La autenticación ahora es manejada por allauth y las vistas de la app 'api'
    path('api/auth/', include('allauth.urls')),

    # Rutas de Administración
    path("api/admin/", include("api.admin_urls")),
    # Las rutas de 'empresa', 'restaurante' y 'turismo' se gestionan ahora
    # a través del panel "Mi Negocio". Se mantienen las apps por la lógica no migrada.
    path("api/turismo/", include("apps.turismo.urls")),
    path("api/empresa/", include("apps.empresa.urls")),
    path("api/restaurante/", include("apps.restaurante.urls")),

    # Panel "Mi Negocio" para Prestadores
    path("api/v1/mi-negocio/", include("apps.prestadores.urls")),

    # Rutas de la API de la aplicación
    path("api/", include("api.urls")),
]

from apps.turismo.views import PublicDisponibilidadView
urlpatterns.insert(len(urlpatterns) - 1, path("api/public/disponibilidad/<str:app_label>/<str:model>/<int:object_id>/", PublicDisponibilidadView.as_view(), name='public-disponibilidad'))

# Servir archivos multimedia en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

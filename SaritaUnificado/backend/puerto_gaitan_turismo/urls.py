"""
URL configuration for puerto_gaitan_turismo project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import (
    TuristaRegisterView,
    ArtesanoRegisterView,
    AdministradorRegisterView,
    FuncionarioDirectivoRegisterView,
    FuncionarioProfesionalRegisterView
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # --- Rutas de Autenticación ---
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/auth/registration/turista/", TuristaRegisterView.as_view(), name='turista-register'),
    path("api/auth/registration/artesano/", ArtesanoRegisterView.as_view(), name='artesano-register'),
    path("api/auth/registration/administrador/", AdministradorRegisterView.as_view(), name='administrador-register'),
    path("api/auth/registration/funcionario_directivo/", FuncionarioDirectivoRegisterView.as_view(), name='funcionario-directivo-register'),
    path("api/auth/registration/funcionario_profesional/", FuncionarioProfesionalRegisterView.as_view(), name='funcionario-profesional-register'),

    # --- Panel del Prestador "Mi Negocio" v1 ---
    path("api/v1/mi-negocio/", include("api.mi_negocio_urls")),

    # --- Rutas Públicas y de Administración ---
    path("api/admin/", include("api.admin_urls")),
    path("api/restaurante/", include("restaurante.urls")), # Se mantiene por ahora para no romper TPV
    path("api/", include("api.urls")), # Rutas públicas y de perfil
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
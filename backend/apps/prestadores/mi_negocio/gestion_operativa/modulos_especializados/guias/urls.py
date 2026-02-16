from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GuiaTuristicoViewSet, CertificacionGuiaViewSet, LocalRutaTuristicaViewSet,
    ItinerarioViewSet, GrupoTuristicoViewSet, ServicioGuiadoViewSet,
    LiquidacionGuiaViewSet, IncidenciaServicioViewSet, SkillViewSet
)

router = DefaultRouter()
router.register(r'perfiles', GuiaTuristicoViewSet, basename='guia-perfiles')
router.register(r'certificaciones', CertificacionGuiaViewSet, basename='guia-certificaciones')
router.register(r'rutas-locales', LocalRutaTuristicaViewSet, basename='guia-rutas-locales')
router.register(r'itinerarios', ItinerarioViewSet, basename='guia-itinerarios')
router.register(r'grupos', GrupoTuristicoViewSet, basename='guia-grupos')
router.register(r'servicios', ServicioGuiadoViewSet, basename='guia-servicios')
router.register(r'liquidaciones', LiquidacionGuiaViewSet, basename='guia-liquidaciones')
router.register(r'incidencias', IncidenciaServicioViewSet, basename='guia-incidencias')
router.register(r'skills', SkillViewSet, basename='guia-skills')

urlpatterns = [
    path('', include(router.urls)),
]

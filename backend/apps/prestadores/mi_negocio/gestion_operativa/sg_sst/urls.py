from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatrizRiesgoViewSet, IncidenteLaboralViewSet, SaludOcupacionalViewSet, CapacitacionSSTViewSet

router = DefaultRouter()
router.register(r'matriz-riesgos', MatrizRiesgoViewSet, basename='matrizriesgo')
router.register(r'incidentes-laborales', IncidenteLaboralViewSet, basename='incidentelaboral')
router.register(r'salud-ocupacional', SaludOcupacionalViewSet, basename='saludocupacional')
router.register(r'capacitaciones', CapacitacionSSTViewSet, basename='capacitacionsst')

urlpatterns = [
    path('', include(router.urls)),
]

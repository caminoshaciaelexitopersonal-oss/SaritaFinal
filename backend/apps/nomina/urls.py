from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, ConceptoNominaViewSet, NominaViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet, basename='empleado')
router.register(r'conceptos', ConceptoNominaViewSet, basename='concepto')
router.register(r'nominas', NominaViewSet, basename='nomina')

urlpatterns = [path('', include(router.urls))]

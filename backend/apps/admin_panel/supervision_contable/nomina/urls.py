from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, ContratoViewSet, PlanillaViewSet, ConceptoNominaViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet, basename='empleado')
router.register(r'contratos', ContratoViewSet, basename='contrato')
router.register(r'planillas', PlanillaViewSet, basename='planilla')
router.register(r'conceptos', ConceptoNominaViewSet, basename='concepto-nomina')

urlpatterns = router.urls

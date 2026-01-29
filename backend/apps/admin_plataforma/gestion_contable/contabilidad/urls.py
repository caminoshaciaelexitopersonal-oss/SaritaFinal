from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanDeCuentasViewSet, CuentaViewSet, PeriodoContableViewSet, AsientoContableViewSet

router = DefaultRouter()
router.register(r'planes', PlanDeCuentasViewSet, basename='plan-de-cuentas')
router.register(r'cuentas', CuentaViewSet, basename='cuenta')
router.register(r'periodos', PeriodoContableViewSet, basename='periodo')
router.register(r'asientos', AsientoContableViewSet, basename='asiento')

urlpatterns = [
    path('', include(router.urls)),
]

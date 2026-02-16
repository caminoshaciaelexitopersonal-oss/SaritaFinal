# backend/apps/prestadores/mi_negocio/gestion_contable/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PlanDeCuentasViewSet,
    CuentaViewSet,
    PeriodoContableViewSet,
    AsientoContableViewSet,
)

# Creamos un router para registrar nuestros ViewSets
router = DefaultRouter()
router.register(r'planes-de-cuentas', PlanDeCuentasViewSet, basename='plan-de-cuentas')
router.register(r'plan-cuentas', PlanDeCuentasViewSet, basename='plan-cuentas-alias')
router.register(r'cuentas', CuentaViewSet, basename='cuenta')
router.register(r'periodos', PeriodoContableViewSet, basename='periodo')
router.register(r'asientos', AsientoContableViewSet, basename='asiento')
router.register(r'comprobantes', AsientoContableViewSet, basename='comprobantes-alias')

# Las URLs de la API son determinadas automáticamente por el router.
urlpatterns = [
    path('', include(router.urls)),
]

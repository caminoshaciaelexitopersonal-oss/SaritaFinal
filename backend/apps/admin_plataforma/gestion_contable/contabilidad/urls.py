from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanDeCuentasViewSet, CuentaViewSet, PeriodoContableViewSet, AsientoContableViewSet

router = DefaultRouter()
router.register(r'charts-of-accounts', PlanDeCuentasViewSet, basename='admin-chart-of-accounts')
router.register(r'accounts', CuentaViewSet, basename='admin-account')
router.register(r'fiscal-periods', PeriodoContableViewSet, basename='admin-fiscal-period')
router.register(r'journal-entries', AsientoContableViewSet, basename='admin-journal-entry')

urlpatterns = [
    path('', include(router.urls)),
]

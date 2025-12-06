from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChartOfAccountViewSet, JournalEntryViewSet, CostCenterViewSet

router = DefaultRouter()
router.register(r'plan-cuentas', ChartOfAccountViewSet, basename='plan-cuentas')
router.register(r'centros-costo', CostCenterViewSet, basename='centro-costo')
router.register(r'asientos-contables', JournalEntryViewSet, basename='asiento-contable')

urlpatterns = [
    path('', include(router.urls)),
]

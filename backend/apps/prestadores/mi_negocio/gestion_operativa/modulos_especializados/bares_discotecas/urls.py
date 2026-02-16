from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NightclubProfileViewSet, NightEventViewSet, NightZoneViewSet,
    NightTableViewSet, NightConsumptionViewSet, LiquorInventoryViewSet,
    InventoryMovementViewSet, CashClosingViewSet, EventLiquidationViewSet
)

router = DefaultRouter()
router.register(r'perfil', NightclubProfileViewSet, basename='nightclub-perfil')
router.register(r'eventos', NightEventViewSet, basename='nightclub-eventos')
router.register(r'zonas', NightZoneViewSet, basename='nightclub-zonas')
router.register(r'mesas', NightTableViewSet, basename='nightclub-mesas')
router.register(r'consumos', NightConsumptionViewSet, basename='nightclub-consumos')
router.register(r'inventario-licores', LiquorInventoryViewSet, basename='nightclub-inventario')
router.register(r'movimientos', InventoryMovementViewSet, basename='nightclub-movimientos')
router.register(r'cierres-caja', CashClosingViewSet, basename='nightclub-cierres')
router.register(r'liquidaciones', EventLiquidationViewSet, basename='nightclub-liquidaciones')

urlpatterns = [
    path('', include(router.urls)),
]

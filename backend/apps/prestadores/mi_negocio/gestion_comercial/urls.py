from rest_framework.routers import DefaultRouter
from .views import FacturaVentaViewSet, ReciboCajaViewSet

router = DefaultRouter()
router.register(r'facturas-venta', FacturaVentaViewSet, basename='factura-venta')
router.register(r'recibos-caja', ReciboCajaViewSet, basename='recibo-caja')

urlpatterns = router.urls

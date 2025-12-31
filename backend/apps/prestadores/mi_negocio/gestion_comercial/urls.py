from rest_framework.routers import DefaultRouter
from .presentation.views import FacturaVentaViewSet

router = DefaultRouter()
router.register(r'facturas-venta', FacturaVentaViewSet, basename='factura-venta')

urlpatterns = router.urls

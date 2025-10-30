# backend/apps/comercial/urls.py
from rest_framework.routers import DefaultRouter
from .views import FacturaVentaViewSet

router = DefaultRouter()
router.register(r'facturas-venta', FacturaVentaViewSet, basename='facturaventa')

urlpatterns = router.urls

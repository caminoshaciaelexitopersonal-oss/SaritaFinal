
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .presentation.views import OperacionComercialAdminViewSet, FacturaVentaAdminViewSet

router = DefaultRouter()
router.register(r'operaciones-comerciales', OperacionComercialAdminViewSet, basename='operacion-comercial-admin')
router.register(r'facturas-venta', FacturaVentaAdminViewSet, basename='factura-venta-admin')

urlpatterns = [
    path('', include(router.urls)),
]

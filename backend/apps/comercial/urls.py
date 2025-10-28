# backend/apps/comercial/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, FacturaVentaViewSet, PagoRecibidoViewSet, NotaCreditoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'facturas-venta', FacturaVentaViewSet, basename='facturaventa')
router.register(r'pagos-recibidos', PagoRecibidoViewSet, basename='pagorecibido')
router.register(r'notas-credito', NotaCreditoViewSet, basename='notacredito')

urlpatterns = [
    path('', include(router.urls)),
]

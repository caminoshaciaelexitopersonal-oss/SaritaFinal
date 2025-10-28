# backend/apps/compras/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, FacturaProveedorViewSet, PagoRealizadoViewSet

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet, basename='proveedor')
router.register(r'facturas-proveedor', FacturaProveedorViewSet, basename='facturaproveedor')
router.register(r'pagos-realizados', PagoRealizadoViewSet, basename='pagorealizado')

urlpatterns = [
    path('', include(router.urls)),
]

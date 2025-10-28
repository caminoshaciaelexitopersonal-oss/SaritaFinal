# backend/apps/compras/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, FacturaProveedorViewSet

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet, basename='proveedor')
router.register(r'facturas-proveedor', FacturaProveedorViewSet, basename='facturaproveedor')

urlpatterns = [
    path('', include(router.urls)),
]

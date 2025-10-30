# backend/apps/comercial/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, FacturaVentaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'facturas-venta', FacturaVentaViewSet, basename='facturaventa')

urlpatterns = [
    path('', include(router.urls)),
]

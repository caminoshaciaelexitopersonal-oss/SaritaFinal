from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .presentation.views import FacturaVentaViewSet, OperacionComercialViewSet

router = DefaultRouter()
router.register(r'operaciones-comerciales', OperacionComercialViewSet, basename='operacion-comercial')
router.register(r'facturas-venta', FacturaVentaViewSet, basename='factura-venta')

urlpatterns = [
    path('', include(router.urls)),
    path('sales/', include('apps.prestadores.mi_negocio.gestion_comercial.sales.urls')),
]

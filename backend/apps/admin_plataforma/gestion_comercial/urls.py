from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .presentation.views import FacturaVentaViewSet

router = DefaultRouter()
router.register(r'facturas-venta', FacturaVentaViewSet, basename='factura-venta')

urlpatterns = [
    path('', include(router.urls)),
    path('domain/', include('apps.admin_plataforma.gestion_comercial.domain.urls')),
]

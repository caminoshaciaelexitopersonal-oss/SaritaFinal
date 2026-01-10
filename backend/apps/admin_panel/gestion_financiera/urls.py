
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .admin_views import CuentaBancariaAdminViewSet, OrdenPagoAdminViewSet

router = DefaultRouter()
router.register(r'cuentas-bancarias', CuentaBancariaAdminViewSet, basename='cuenta-bancaria-admin')
router.register(r'ordenes-pago', OrdenPagoAdminViewSet, basename='orden-pago-admin')

urlpatterns = [
    path('', include(router.urls)),
]

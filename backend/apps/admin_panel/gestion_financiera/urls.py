
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .admin_views import CuentaBancariaViewSet, OrdenPagoViewSet

router = DefaultRouter()
router.register(r'cuentas-bancarias', CuentaBancariaViewSet, basename='cuenta-bancaria-admin')
router.register(r'ordenes-pago', OrdenPagoViewSet, basename='orden-pago-admin')

urlpatterns = [
    path('', include(router.urls)),
]

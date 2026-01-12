
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .admin_views import CuentaBancariaViewSet, OrdenPagoViewSet

router = DefaultRouter()
router.register(r'cuentas-bancarias', CuentaBancariaViewSet, basename='cuentas-bancarias-admin')
router.register(r'ordenes-pago', OrdenPagoViewSet, basename='ordenes-pago-admin')

urlpatterns = [
    path('', include(router.urls)),
]

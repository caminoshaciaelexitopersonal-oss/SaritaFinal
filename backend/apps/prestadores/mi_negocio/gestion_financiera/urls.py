from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuentaBancariaViewSet, TransaccionBancariaViewSet

router = DefaultRouter()
router.register(r'cuentas-bancarias', CuentaBancariaViewSet, basename='cuenta-bancaria')
router.register(r'transacciones-bancarias', TransaccionBancariaViewSet, basename='transaccion-bancaria')

urlpatterns = [
    path('', include(router.urls)),
]

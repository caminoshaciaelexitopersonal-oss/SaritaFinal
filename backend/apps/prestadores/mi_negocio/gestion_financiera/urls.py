from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CuentaBancariaViewSet, TransaccionBancariaViewSet, ReporteIngresosGastosView

router = DefaultRouter()
router.register(r'cuentas-bancarias', CuentaBancariaViewSet, basename='cuenta-bancaria')
router.register(r'transacciones', TransaccionBancariaViewSet, basename='transaccion-bancaria')

urlpatterns = router.urls

urlpatterns += [
    path('reporte-ingresos-gastos/', ReporteIngresosGastosView.as_view(), name='reporte-ingresos-gastos'),
]

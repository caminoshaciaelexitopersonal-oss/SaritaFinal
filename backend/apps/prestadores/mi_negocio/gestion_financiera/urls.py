from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'cuentas-bancarias', CuentaBancariaViewSet, basename='cuentabancaria')
router.register(r'ordenes-pago', OrdenPagoViewSet, basename='ordenpago')
router.register(r'tesoreria', TesoreriaCentralViewSet, basename='tesoreria')
router.register(r'estado-resultados', EstadoResultadosViewSet, basename='estadoresultados')
router.register(r'balance-general', BalanceGeneralViewSet, basename='balancegeneral')
router.register(r'proyecciones', ProyeccionFinancieraViewSet, basename='proyeccion')
router.register(r'riesgos', RiesgoFinancieroViewSet, basename='riesgo')

urlpatterns = [
    path('', include(router.urls)),
]

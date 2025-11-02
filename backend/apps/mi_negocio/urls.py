
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.mi_negocio.gestion_operativa.modulos_genericos.clientes.views import ClienteViewSet
from apps.contabilidad.views import ChartOfAccountViewSet, JournalEntryViewSet
from apps.financiero.views import BankAccountViewSet, CashTransactionViewSet
from apps.comercial.views import ProductoViewSet, FacturaVentaViewSet
from api.views import PlaceholderView

app_name = 'mi_negocio'

router = DefaultRouter()
router.register(r'operativa/clientes', ClienteViewSet, basename='cliente')
router.register(r'contable/plan-de-cuentas', ChartOfAccountViewSet, basename='plan-de-cuentas')
router.register(r'contable/asientos', JournalEntryViewSet, basename='asiento-contable')
router.register(r'financiera/cuentas-bancarias', BankAccountViewSet, basename='cuenta-bancaria')
router.register(r'financiera/transacciones', CashTransactionViewSet, basename='transaccion-financiera')
router.register(r'comercial/productos', ProductoViewSet, basename='producto')
router.register(r'comercial/facturas', FacturaVentaViewSet, basename='factura-venta')

urlpatterns = [
    path('', include(router.urls)),
    # Rutas de marcador de posición para los otros módulos
    path('archivistica/', PlaceholderView.as_view(), name='archivistica-placeholder'),
]

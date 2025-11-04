from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BankAccountViewSet, CashTransactionViewSet, ReporteIngresosGastosView

router = DefaultRouter()
router.register(r'bank-accounts', BankAccountViewSet, basename='bank-account')
router.register(r'cash-transactions', CashTransactionViewSet, basename='cash-transaction')

urlpatterns = router.urls

urlpatterns += [
    path('reporte-ingresos-gastos/', ReporteIngresosGastosView.as_view(), name='reporte-ingresos-gastos'),
]

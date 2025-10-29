from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.financiera.views import BankAccountViewSet, CashTransactionViewSet

router = DefaultRouter()
router.register(r'cuentas-bancarias', BankAccountViewSet, basename='bank-accounts')
router.register(r'transacciones', CashTransactionViewSet, basename='cash-transactions')

urlpatterns = [
    path('', include(router.urls)),
]

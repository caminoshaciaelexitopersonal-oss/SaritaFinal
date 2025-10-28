# backend/apps/financiera/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BankAccountViewSet, CashTransactionViewSet

router = DefaultRouter()
router.register(r'bank-accounts', BankAccountViewSet, basename='bankaccount')
router.register(r'cash-transactions', CashTransactionViewSet, basename='cashtransaction')

urlpatterns = [
    path('', include(router.urls)),
]

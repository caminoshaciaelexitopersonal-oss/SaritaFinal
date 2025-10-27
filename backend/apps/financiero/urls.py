# backend/apps/financiero/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bank-accounts', views.BankAccountViewSet, basename='bank-account')
router.register(r'cash-transactions', views.CashTransactionViewSet, basename='cash-transaction')

urlpatterns = [
    path('', include(router.urls)),
]

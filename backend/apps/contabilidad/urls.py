# backend/apps/contabilidad/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cost-centers', views.CostCenterViewSet, basename='cost-center')
router.register(r'chart-of-accounts', views.ChartOfAccountViewSet, basename='chart-of-account')
router.register(r'journal-entries', views.JournalEntryViewSet, basename='journal-entry')
router.register(r'currencies', views.CurrencyViewSet, basename='currency')

urlpatterns = [
    path('', include(router.urls)),
]

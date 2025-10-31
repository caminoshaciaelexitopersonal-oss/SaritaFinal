# backend/apps/contabilidad/urls.py
from django.urls import path, include; from rest_framework.routers import DefaultRouter; from . import views
router = DefaultRouter(); router.register(r'chart-of-accounts', views.ChartOfAccountViewSet); router.register(r'journal-entries', views.JournalEntryViewSet); router.register(r'currencies', views.CurrencyViewSet)
urlpatterns = [path('', include(router.urls)), path('informes/', include('.urls_reports'))]

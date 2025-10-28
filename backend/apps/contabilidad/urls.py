# backend/apps/contabilidad/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'chart-of-accounts', views.ChartOfAccountViewSet, basename='chartofaccount')
router.register(r'journal-entries', views.JournalEntryViewSet, basename='journalentry')
router.register(r'cost-centers', views.CostCenterViewSet, basename='costcenter')

app_name = 'contabilidad_api'

urlpatterns = [
    path('', include(router.urls)),
]

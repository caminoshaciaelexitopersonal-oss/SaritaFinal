# SaritaUnificado/backend/apps/comercial/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacturaVentaViewSet

router = DefaultRouter()
router.register(r'facturasventa', FacturaVentaViewSet, basename='facturaventa')

urlpatterns = [
    path('', include(router.urls)),
]

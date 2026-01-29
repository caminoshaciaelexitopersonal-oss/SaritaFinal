from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacturaVentaSystemicViewSet

router = DefaultRouter()
router.register(r'facturas', FacturaVentaSystemicViewSet, basename='systemic-facturas')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import VehicleViewSet #, MaintenanceOrderViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
# router.register(r'maintenance-orders', MaintenanceOrderViewSet, basename='maintenance-order')

urlpatterns = [
    path('', include(router.urls)),
]

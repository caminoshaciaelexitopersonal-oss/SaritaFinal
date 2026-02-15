from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, TransportRouteViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='transport-vehicle')
router.register(r'routes', TransportRouteViewSet, basename='transport-route')

urlpatterns = [
    path('', include(router.urls)),
]

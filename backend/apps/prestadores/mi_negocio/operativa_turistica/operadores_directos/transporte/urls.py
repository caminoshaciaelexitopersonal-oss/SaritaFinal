from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VehicleViewSet, ConductorViewSet, TransportRouteViewSet,
    ScheduledTripViewSet, TransportBookingViewSet,
    TripLiquidationViewSet, TransportIncidentViewSet
)

router = DefaultRouter()
router.register(r'vehiculos', VehicleViewSet, basename='transport-vehiculos')
router.register(r'conductores', ConductorViewSet, basename='transport-conductores')
router.register(r'rutas', TransportRouteViewSet, basename='transport-rutas')
router.register(r'viajes', ScheduledTripViewSet, basename='transport-viajes')
router.register(r'reservas', TransportBookingViewSet, basename='transport-reservas')
router.register(r'liquidaciones', TripLiquidationViewSet, basename='transport-liquidaciones')
router.register(r'incidencias', TransportIncidentViewSet, basename='transport-incidencias')

urlpatterns = [
    path('', include(router.urls)),
]

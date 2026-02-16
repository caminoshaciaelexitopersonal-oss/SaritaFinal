from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Vehicle, VehicleCertification, Conductor, TransportRoute,
    ScheduledTrip, TransportBooking, TripLiquidation, TransportIncident
)
from .serializers import *

class TransportBaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(provider=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user.perfil_prestador)

class VehicleViewSet(TransportBaseViewSet):
    model = Vehicle
    serializer_class = VehicleSerializer

class ConductorViewSet(TransportBaseViewSet):
    model = Conductor
    serializer_class = ConductorSerializer

class TransportRouteViewSet(TransportBaseViewSet):
    model = TransportRoute
    serializer_class = TransportRouteSerializer

class ScheduledTripViewSet(TransportBaseViewSet):
    model = ScheduledTrip
    serializer_class = ScheduledTripSerializer

    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        trip = self.get_object()
        if not trip.vehiculo or not trip.conductor:
            return Response({'error': 'Falta vehículo o conductor asignado'}, status=status.HTTP_400_BAD_REQUEST)

        trip.estado = ScheduledTrip.TripStatus.CONFIRMADO
        trip.save()
        return Response({'status': 'Viaje confirmado'})

class TransportBookingViewSet(TransportBaseViewSet):
    model = TransportBooking
    serializer_class = TransportBookingSerializer

class TripLiquidationViewSet(TransportBaseViewSet):
    model = TripLiquidation
    serializer_class = TripLiquidationSerializer

class TransportIncidentViewSet(TransportBaseViewSet):
    model = TransportIncident
    serializer_class = TransportIncidentSerializer

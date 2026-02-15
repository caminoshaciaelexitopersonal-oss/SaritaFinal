from rest_framework import viewsets, permissions
from .models import Vehicle, TransportRoute
from .serializers import VehicleSerializer, TransportRouteSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Vehicle.objects.filter(provider=self.request.user.perfil_prestador)

class TransportRouteViewSet(viewsets.ModelViewSet):
    serializer_class = TransportRouteSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return TransportRoute.objects.filter(provider=self.request.user.perfil_prestador)

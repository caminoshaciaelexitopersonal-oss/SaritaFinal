from rest_framework import viewsets, permissions
from ..models.provider_models import TourismProvider, BusinessProfile, TourismService, Reservation
from ..serializers.provider_serializers import (
    TourismProviderSerializer, BusinessProfileSerializer,
    TourismServiceSerializer, ReservationSerializer
)

class TourismProviderViewSet(viewsets.ModelViewSet):
    queryset = TourismProvider.objects.all()
    serializer_class = TourismProviderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Cada dueño solo ve sus propios prestadores
        if self.request.user.is_staff:
            return TourismProvider.objects.all()
        return TourismProvider.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BusinessProfileViewSet(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class TourismServiceViewSet(viewsets.ModelViewSet):
    queryset = TourismService.objects.all()
    serializer_class = TourismServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

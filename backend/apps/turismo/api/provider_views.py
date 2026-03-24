from django.db import models
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.provider_models import TourismProvider, BusinessProfile, TourismService, Reservation
from ..serializers.provider_serializers import (
    TourismProviderSerializer, BusinessProfileSerializer,
    TourismServiceSerializer, ReservationSerializer
)
from ..services.financial_service import TourismFinancialService

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

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Reservation.objects.all()
        # Turista ve sus reservas, Dueño ve las reservas de sus prestadores
        return Reservation.objects.filter(
            models.Q(customer=user) | models.Q(provider__owner=user)
        ).distinct()

    @action(detail=True, methods=['post'])
    def process_payment(self, request, pk=None):
        """
        Inicia el flujo de pago de la reserva.
        """
        try:
            result = TourismFinancialService.process_reservation_payment(pk)
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from ..models import CustomUser, GovernmentProfile, TouristProfile, DeliveryProfile
from .serializers import GovernmentProfileSerializer, TouristProfileSerializer, DeliveryProfileSerializer, BusinessUserSerializer
from apps.turismo.models.provider_models import TourismProvider

class GovernmentProfileViewSet(viewsets.ModelViewSet):
    queryset = GovernmentProfile.objects.all()
    serializer_class = GovernmentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Flujo 1-3: El directivo crea al funcionario
        serializer.save(created_by=self.request.user)

class TouristProfileViewSet(viewsets.ModelViewSet):
    queryset = TouristProfile.objects.all()
    serializer_class = TouristProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeliveryProfileViewSet(viewsets.ModelViewSet):
    queryset = DeliveryProfile.objects.all()
    serializer_class = DeliveryProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class BusinessProfileViewSet(viewsets.ModelViewSet):
    queryset = TourismProvider.objects.all()
    serializer_class = BusinessUserSerializer
    permission_classes = [permissions.IsAuthenticated]

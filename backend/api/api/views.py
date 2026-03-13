from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from ..models import CustomUser, GovernmentProfile, TouristProfile, DeliveryProfile, BusinessUserProfile
from .serializers import (
    GovernmentProfileSerializer, TouristProfileSerializer,
    DeliveryProfileSerializer, BusinessUserSerializer,
    UserMinimalSerializer, BusinessProfileSerializer
)
from apps.turismo.models.provider_models import TourismProvider
from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserMinimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == CustomUser.Role.ADMIN:
            return CustomUser.objects.all()

        # Filtro jerárquico básico
        if user.role in [CustomUser.Role.DIRECTIVO_NACIONAL, CustomUser.Role.ADMIN_NACIONAL]:
            return CustomUser.objects.all()

        if user.role in [CustomUser.Role.DIRECTIVO_DEPARTAMENTAL, CustomUser.Role.ADMIN_DEPARTAMENTAL]:
            return CustomUser.objects.exclude(role__in=[CustomUser.Role.ADMIN_NACIONAL, CustomUser.Role.DIRECTIVO_NACIONAL])

        return CustomUser.objects.filter(id=user.id)

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
    """
    Endpoint para ver la lista de Prestadores (Empresas)
    """
    queryset = TourismProvider.objects.all()
    serializer_class = BusinessUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BusinessStaffViewSet(viewsets.ModelViewSet):
    """
    Endpoint para gestionar el personal de los negocios (Vía 2)
    """
    queryset = BusinessUserProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == CustomUser.Role.BUSINESS_OWNER:
            return BusinessUserProfile.objects.filter(provider__owner=user)
        return BusinessUserProfile.objects.all()

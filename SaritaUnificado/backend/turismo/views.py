from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, Habitacion, GuiaTuristico, VehiculoTuristico, PaqueteTuristico
from .serializers import HotelSerializer, HabitacionSerializer, GuiaTuristicoSerializer, VehiculoTuristicoSerializer, PaqueteTuristicoSerializer
from api.permissions import IsPrestador, IsPrestadorOwner

class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Hotel.objects.filter(prestador=self.request.user.perfil_prestador)
        return Hotel.objects.none()

    def perform_create(self, serializer):
        # Asumiendo que el perfil de prestador ya existe
        serializer.save(prestador=self.request.user.perfil_prestador)

class HabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacionSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador') and hasattr(self.request.user.perfil_prestador, 'hotel_profile'):
            return Habitacion.objects.filter(hotel=self.request.user.perfil_prestador.hotel_profile)
        return Habitacion.objects.none()

    def perform_create(self, serializer):
        hotel_profile = self.request.user.perfil_prestador.hotel_profile
        serializer.save(hotel=hotel_profile)

class GuiaTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = GuiaTuristicoSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return GuiaTuristico.objects.filter(prestador=self.request.user.perfil_prestador)
        return GuiaTuristico.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class VehiculoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = VehiculoTuristicoSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return VehiculoTuristico.objects.filter(prestador=self.request.user.perfil_prestador)
        return VehiculoTuristico.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class PaqueteTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PaqueteTuristicoSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return PaqueteTuristico.objects.filter(prestador_agencia=self.request.user.perfil_prestador)
        return PaqueteTuristico.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador_agencia=self.request.user.perfil_prestador)
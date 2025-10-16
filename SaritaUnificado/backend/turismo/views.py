from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, Habitacion, Tarifa, Disponibilidad, Reserva
from .serializers import HotelSerializer, HabitacionSerializer, TarifaSerializer, DisponibilidadSerializer, ReservaSerializer
from api.permissions import IsPrestador, IsPrestadorOwner

class TarifaViewSet(viewsets.ModelViewSet):
    serializer_class = TarifaSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Tarifa.objects.filter(prestador=self.request.user.perfil_prestador)
        return Tarifa.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class DisponibilidadViewSet(viewsets.ModelViewSet):
    serializer_class = DisponibilidadSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Disponibilidad.objects.filter(prestador=self.request.user.perfil_prestador)
        return Disponibilidad.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Reserva.objects.filter(prestador=self.request.user.perfil_prestador).select_related('cliente')
        return Reserva.objects.none()

    def perform_create(self, serializer):
        # Aquí iría la lógica para verificar disponibilidad y calcular el monto
        serializer.save(prestador=self.request.user.perfil_prestador)

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
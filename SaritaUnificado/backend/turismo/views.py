 from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, Habitacion, Reserva
from .serializers import HotelSerializer, HabitacionSerializer, ReservaSerializer
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


class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, IsPrestador]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Reserva.objects.filter(prestador=self.request.user.perfil_prestador)
        return Reserva.objects.none()

    def perform_create(self, serializer):
        # Asignar el prestador y, opcionalmente, el cliente si es un usuario registrado
        cliente = serializer.validated_data.get('cliente')
        serializer.save(prestador=self.request.user.perfil_prestador, cliente=cliente)

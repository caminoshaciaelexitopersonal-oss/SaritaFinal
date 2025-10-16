from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Hotel, Habitacion, Tarifa, Disponibilidad, Reserva, RutaTuristica
from .serializers import HotelSerializer, HabitacionSerializer, TarifaSerializer, DisponibilidadSerializer, ReservaSerializer, RutaTuristicaSerializer
from api.permissions import IsPrestador, IsPrestadorOwner
from django.contrib.contenttypes.models import ContentType

class PublicDisponibilidadView(generics.ListAPIView):
    """
    Vista pública para consultar la disponibilidad de un recurso.
    Ej: /api/public/disponibilidad/turismo/habitacion/1/
    """
    serializer_class = DisponibilidadSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        app_label = self.kwargs.get('app_label')
        model = self.kwargs.get('model')
        object_id = self.kwargs.get('object_id')

        try:
            content_type = ContentType.objects.get(app_label=app_label, model=model)
            return Disponibilidad.objects.filter(content_type=content_type, object_id=object_id)
        except ContentType.DoesNotExist:
            return Disponibilidad.objects.none()


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

class PublicHabitacionListView(generics.ListAPIView):
    """
    Vista pública para listar las habitaciones de un hotel específico.
    """
    serializer_class = HabitacionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')
        return Habitacion.objects.filter(hotel_id=hotel_id)

class RutaTuristicaViewSet(viewsets.ModelViewSet):
    serializer_class = RutaTuristicaSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return RutaTuristica.objects.filter(prestadores=self.request.user.perfil_prestador)
        return RutaTuristica.objects.none()

    def perform_create(self, serializer):
        # Asigna automáticamente el prestador (guía) a la ruta.
        instance = serializer.save()
        instance.prestadores.add(self.request.user.perfil_prestador)

class RutaTuristicaViewSet(viewsets.ModelViewSet):
    serializer_class = RutaTuristicaSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return RutaTuristica.objects.filter(prestadores=self.request.user.perfil_prestador)
        return RutaTuristica.objects.none()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.prestadores.add(self.request.user.perfil_prestador)

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
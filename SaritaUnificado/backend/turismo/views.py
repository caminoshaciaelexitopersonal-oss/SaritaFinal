from rest_framework import viewsets, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db import transaction, models
from datetime import timedelta
from .models import Hotel, Habitacion, Tarifa, Disponibilidad, Reserva
from api.models import RutaTuristica #, VehiculoTuristico, PaqueteTuristico
from .serializers import HotelSerializer, HabitacionSerializer, TarifaSerializer, DisponibilidadSerializer, ReservaSerializer, RutaTuristicaSerializer #, VehiculoTuristicoSerializer, PaqueteTuristicoSerializer
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


# --- Vistas para el Módulo de Tarifas (RAT) ---
class TarifaViewSet(viewsets.ModelViewSet):
    """
    Gestiona las tarifas de un prestador para diferentes recursos.
    """
    serializer_class = TarifaSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Tarifa.objects.filter(prestador=self.request.user.perfil_prestador)
        return Tarifa.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

# --- Vistas para el Módulo de Disponibilidad (RAT) ---
class DisponibilidadViewSet(viewsets.ModelViewSet):
    """
    Gestiona la disponibilidad de un prestador para diferentes recursos.
    """
    serializer_class = DisponibilidadSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Disponibilidad.objects.filter(prestador=self.request.user.perfil_prestador)
        return Disponibilidad.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

# --- Vistas para el Módulo de Reservas (RAT) ---
class ReservaViewSet(viewsets.ModelViewSet):
    """
    Gestiona las reservas de un prestador.
    """
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            # El prestador ve las reservas de sus servicios
            return Reserva.objects.filter(prestador=user.perfil_prestador).select_related('cliente', 'content_type')
        if not user.is_staff and not user.is_superuser:
            # Un turista ve sus propias reservas
            return Reserva.objects.filter(cliente__usuario=user).select_related('cliente', 'content_type')
        return Reserva.objects.none()

    @transaction.atomic
    def perform_create(self, serializer):
        content_type = serializer.validated_data.get('content_type')
        object_id = serializer.validated_data.get('object_id')
        fecha_inicio = serializer.validated_data.get('fecha_inicio_reserva')
        fecha_fin = serializer.validated_data.get('fecha_fin_reserva')

        if not all([content_type, object_id, fecha_inicio, fecha_fin]):
            raise ValidationError("Faltan datos para procesar la reserva (recurso, fechas).")

        # 1. Verificar disponibilidad para cada día del rango
        dias_a_verificar = []
        current_date = fecha_inicio.date()
        while current_date < fecha_fin.date():
            dias_a_verificar.append(current_date)
            current_date += timedelta(days=1)

        if not dias_a_verificar:
             raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

        disponibilidades = Disponibilidad.objects.filter(
            content_type=content_type,
            object_id=object_id,
            fecha__in=dias_a_verificar
        ).select_for_update() # Bloquear filas para evitar race conditions

        if len(disponibilidades) != len(dias_a_verificar):
            raise ValidationError("No existe un registro de disponibilidad para una o más de las fechas solicitadas.")

        for d in disponibilidades:
            if d.cupos_disponibles < 1:
                raise ValidationError(f"No hay cupos disponibles para el día {d.fecha}.")

        # 2. Calcular el monto total basado en la tarifa
        recurso_reservado = content_type.get_object_for_this_type(id=object_id)
        tarifa = Tarifa.objects.filter(
            content_type=content_type,
            object_id=object_id,
            fecha_inicio__lte=fecha_inicio.date(),
            fecha_fin__gte=fecha_fin.date()
        ).first()

        if tarifa:
            precio_base = tarifa.precio
        elif hasattr(recurso_reservado, 'precio_por_noche'):
            precio_base = recurso_reservado.precio_por_noche
        elif hasattr(recurso_reservado, 'precio'):
             precio_base = recurso_reservado.precio
        else:
            raise ValidationError("No se encontró una tarifa aplicable para el recurso y las fechas seleccionadas.")

        monto_total_calculado = precio_base * len(dias_a_verificar)

        # 3. Guardar la reserva y actualizar la disponibilidad
        serializer.save(
            prestador=self.request.user.perfil_prestador,
            monto_total=monto_total_calculado
        )

        # Actualizar cupos ocupados
        for d in disponibilidades:
            d.cupos_ocupados = models.F('cupos_ocupados') + 1
            d.save(update_fields=['cupos_ocupados'])

# --- Vistas para el Módulo de Hotel ---
class HotelViewSet(viewsets.ModelViewSet):
    """
    Gestiona el perfil de un hotel.
    """
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

# --- Vistas para el Módulo de Guías Turísticos ---
class RutaTuristicaViewSet(viewsets.ModelViewSet):
    """
    Gestiona las rutas de un guía turístico.
    """
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

# --- Vistas para el Módulo de Habitaciones (Hotel) ---
class HabitacionViewSet(viewsets.ModelViewSet):
    """
    Gestiona las habitaciones de un hotel.
    """
    serializer_class = HabitacionSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador') and hasattr(self.request.user.perfil_prestador, 'hotel_profile'):
            return Habitacion.objects.filter(hotel=self.request.user.perfil_prestador.hotel_profile)
        return Habitacion.objects.none()

    def perform_create(self, serializer):
        hotel_profile = self.request.user.perfil_prestador.hotel_profile
        serializer.save(hotel=hotel_profile)
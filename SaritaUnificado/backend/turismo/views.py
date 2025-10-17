# turismo/views.py

# --- Vistas de la App TURISMO ---
# Nota: La lógica del panel de prestadores (Hotel, Reservas, RAT, etc.) ha sido
# centralizada en el enrutador de 'mi_negocio'.
# Esta app ahora contiene principalmente la lógica de la oferta turística
# y las vistas públicas.

from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import GuiaTuristico, VehiculoTuristico, PaqueteTuristico, Habitacion
from .serializers import GuiaTuristicoSerializer, VehiculoTuristicoSerializer, PaqueteTuristicoSerializer, HabitacionSerializer
from api.permissions import IsPrestador, IsPrestadorOwner

# --- Vistas para el Panel de Prestador (gestionadas por el router de mi_negocio) ---

class HotelViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass

class HabitacionViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass

class TarifaViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass

class DisponibilidadViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass

class ReservaViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass

class RutaTuristicaViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass

class VehiculoTuristicoViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass

class PaqueteTuristicoViewSet(viewsets.ModelViewSet):
    # ... (código movido a mi_negocio)
    pass


# --- Vistas Públicas ---

class PublicHabitacionListView(generics.ListAPIView):
    """
    Vista pública para listar las habitaciones de un hotel específico.
    """
    serializer_class = HabitacionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')
        # La lógica para obtener el hotel desde el prestador ID se manejará aquí
        # Por ahora, se asume que hotel_id es el pk del prestador
        return Habitacion.objects.filter(hotel__prestador_id=hotel_id)
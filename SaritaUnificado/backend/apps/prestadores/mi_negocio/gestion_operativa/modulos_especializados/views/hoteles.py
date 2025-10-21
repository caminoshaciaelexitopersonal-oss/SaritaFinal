# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/views/hoteles.py
from ...modulos_genericos.views.base import GenericViewSet
from apps.prestadores.models import Habitacion, ServicioAdicionalHotel
from ..serializers.hoteles import HabitacionSerializer, ServicioAdicionalHotelSerializer

class HabitacionViewSet(GenericViewSet):
    """
    API endpoint para gestionar las Habitaciones de un hotel.
    """
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class ServicioAdicionalHotelViewSet(GenericViewSet):
    """
    API endpoint para gestionar los Servicios Adicionales de un hotel.
    """
    queryset = ServicioAdicionalHotel.objects.all()
    serializer_class = ServicioAdicionalHotelSerializer

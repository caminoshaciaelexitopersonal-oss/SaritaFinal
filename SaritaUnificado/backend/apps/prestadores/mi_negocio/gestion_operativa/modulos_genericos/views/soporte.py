# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/soporte.py
from .base import GenericViewSet
from apps.prestadores.models import TicketSoporte
from ..serializers.soporte import TicketSoporteSerializer

class TicketSoporteViewSet(GenericViewSet):
    queryset = TicketSoporte.objects.all()
    serializer_class = TicketSoporteSerializer

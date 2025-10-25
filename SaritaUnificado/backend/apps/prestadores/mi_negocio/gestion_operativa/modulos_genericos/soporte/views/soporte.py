# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/soporte.py
from ...views.base import GenericViewSet
from ..models.soporte import TicketSoporte
from ..serializers.soporte import TicketSoporteSerializer

class TicketSoporteViewSet(GenericViewSet):
    queryset = TicketSoporte.objects.all()
    serializer_class = TicketSoporteSerializer

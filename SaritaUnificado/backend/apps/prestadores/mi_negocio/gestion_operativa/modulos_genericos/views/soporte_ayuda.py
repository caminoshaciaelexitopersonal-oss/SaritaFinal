from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.soporte_ayuda import TicketSoporte
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.soporte_ayuda import TicketSoporteSerializer

class TicketSoporteViewSet(GenericViewSet):
    """
    API endpoint para gestionar los Tickets de Soporte del prestador.
    """
    queryset = TicketSoporte.objects.all()
    serializer_class = TicketSoporteSerializer

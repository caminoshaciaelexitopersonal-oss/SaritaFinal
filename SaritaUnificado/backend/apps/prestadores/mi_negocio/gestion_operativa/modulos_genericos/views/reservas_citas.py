from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reservas_citas import Reserva
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.reservas_citas import ReservaSerializer

class ReservaViewSet(GenericViewSet):
    """
    API endpoint para gestionar las Reservas del prestador.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

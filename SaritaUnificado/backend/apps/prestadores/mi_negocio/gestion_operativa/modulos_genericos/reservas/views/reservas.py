# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/reservas.py
from ...views.base import GenericViewSet
from ..models.reservas import Reserva
from ..serializers.reservas import ReservaSerializer

class ReservaViewSet(GenericViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

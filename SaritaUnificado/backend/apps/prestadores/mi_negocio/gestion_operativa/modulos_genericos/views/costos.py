from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.costos import Costo
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.costos import CostoSerializer

class CostoViewSet(GenericViewSet):
    """
    API endpoint para gestionar los Costos del prestador.
    """
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer

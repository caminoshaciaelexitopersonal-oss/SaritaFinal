from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.inventario import Inventario
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.inventario import InventarioSerializer

class InventarioViewSet(GenericViewSet):
    """
    API endpoint para gestionar el Inventario del prestador.
    """
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

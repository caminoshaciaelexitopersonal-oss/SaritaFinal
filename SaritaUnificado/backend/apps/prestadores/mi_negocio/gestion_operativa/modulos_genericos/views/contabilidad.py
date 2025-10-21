# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/contabilidad.py
from .base import GenericViewSet
from apps.prestadores.models import Costo, Inventario
from ..serializers.contabilidad import CostoSerializer, InventarioSerializer

class CostoViewSet(GenericViewSet):
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer

class InventarioViewSet(GenericViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

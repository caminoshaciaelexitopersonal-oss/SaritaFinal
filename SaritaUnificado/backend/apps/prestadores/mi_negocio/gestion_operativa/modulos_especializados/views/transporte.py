# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/views/transporte.py
from ...modulos_genericos.views.base import GenericViewSet
from apps.prestadores.models import Vehiculo, Conductor
from ..serializers.transporte import VehiculoSerializer, ConductorSerializer

class VehiculoViewSet(GenericViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class ConductorViewSet(GenericViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

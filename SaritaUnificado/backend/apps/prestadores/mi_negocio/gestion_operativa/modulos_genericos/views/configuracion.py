# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/configuracion.py
from .base import GenericViewSet
from apps.prestadores.models import ConfiguracionPrestador
from ..serializers.configuracion import ConfiguracionPrestadorSerializer

class ConfiguracionPrestadorViewSet(GenericViewSet):
    queryset = ConfiguracionPrestador.objects.all()
    serializer_class = ConfiguracionPrestadorSerializer

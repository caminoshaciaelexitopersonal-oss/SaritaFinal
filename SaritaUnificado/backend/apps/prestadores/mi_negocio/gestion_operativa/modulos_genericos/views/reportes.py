# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/reportes.py
from .base import GenericViewSet
from apps.prestadores.models import Reporte
from ..serializers.reportes import ReporteSerializer

class ReporteViewSet(GenericViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

from rest_framework import mixins, viewsets
from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reportes_estadisticas import Reporte
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.reportes_estadisticas import ReporteSerializer

class ReporteViewSet(viewsets.ReadOnlyModelViewSet, GenericViewSet):
    """
    API endpoint para ver los Reportes del prestador.
    """
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

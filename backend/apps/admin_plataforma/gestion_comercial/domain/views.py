from rest_framework import viewsets
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta
from apps.prestadores.mi_negocio.gestion_comercial.presentation.serializers import FacturaVentaListSerializer

class FacturaVentaSystemicViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para Facturas de Venta en el ámbito del Super Admin (Sistémico).
    """
    queryset = FacturaVenta.objects.all()
    serializer_class = FacturaVentaListSerializer

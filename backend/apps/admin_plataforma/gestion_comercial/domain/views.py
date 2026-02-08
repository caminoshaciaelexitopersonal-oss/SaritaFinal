 
from rest_framework import viewsets, permissions
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_comercial.domain.models import FacturaVenta
from apps.admin_plataforma.gestion_comercial.presentation.serializers import AdminFacturaVentaListSerializer
from api.permissions import IsSuperAdmin
 

class FacturaVentaSystemicViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para Facturas de Venta en el ámbito del Super Admin (Sistémico).
    """
    queryset = FacturaVenta.objects.all()
    serializer_class = AdminFacturaVentaListSerializer
 
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
 

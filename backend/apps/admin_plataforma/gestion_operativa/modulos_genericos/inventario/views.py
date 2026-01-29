from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.inventario.models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para que el Super Admin gestione el inventario sistémico.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)

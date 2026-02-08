from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_operativa.modulos_genericos.clientes.models import Cliente
from .serializers import AdminClienteSerializer

class ClienteViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para que el Super Admin gestione clientes sistémicos.
    """
    queryset = Cliente.objects.all()
    serializer_class = AdminClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)

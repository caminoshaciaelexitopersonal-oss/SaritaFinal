from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_operativa.modulos_genericos.costos.models import Costo
from .serializers import CostoSerializer

class CostoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(perfil=perfil_gobierno)

from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_operativa.modulos_genericos.reservas.models import Reserva, PoliticaCancelacion
from .serializers import AdminReservaSerializer, AdminPoliticaCancelacionSerializer

class ReservaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para que el Super Admin gestione reservas sistémicas.
    """
    queryset = Reserva.objects.all()
    serializer_class = AdminReservaSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)

class PoliticaCancelacionViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = PoliticaCancelacion.objects.all()
    serializer_class = AdminPoliticaCancelacionSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)

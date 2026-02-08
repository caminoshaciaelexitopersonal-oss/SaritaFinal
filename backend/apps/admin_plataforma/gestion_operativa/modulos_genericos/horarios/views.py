from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_operativa.modulos_genericos.horarios.models import Horario, ExcepcionHorario
from .serializers import AdminHorarioSerializer, AdminExcepcionHorarioSerializer

class HorarioViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = AdminHorarioSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(perfil=perfil_gobierno)

class ExcepcionHorarioViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = ExcepcionHorario.objects.all()
    serializer_class = AdminExcepcionHorarioSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(perfil=perfil_gobierno)

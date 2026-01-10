from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Horario, ExcepcionHorario
from .serializers import HorarioSerializer, ExcepcionHorarioSerializer
from apps.prestadores.mi_negocio.permissions import IsPrestadorOwner

class HorarioAdminViewSet(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return .objects.all()

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class ExcepcionHorarioAdminViewSet(viewsets.ModelViewSet):
    serializer_class = ExcepcionHorarioSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return .objects.all()

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

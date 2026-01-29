from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from .serializers import PerfilSerializer, PerfilUpdateSerializer
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin

class PerfilViewSet(SystemicERPViewSetMixin, viewsets.GenericViewSet):
    """
    ViewSet para que el Super Admin gestione el perfil sistémico de la plataforma.
    """
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_object(self):
        return GestionPlataformaService.get_perfil_gobierno()

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        instance = self.get_object()
        if not instance:
            return Response({"detail": "Perfil de plataforma no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PerfilSerializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['put', 'patch'], url_path='update-me')
    def update_me(self, request):
        instance = self.get_object()
        if not instance:
            return Response({"detail": "Perfil de plataforma no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PerfilUpdateSerializer(instance, data=request.data, partial=request.method == 'PATCH')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

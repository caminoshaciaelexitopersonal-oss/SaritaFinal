from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Reserva, PoliticaCancelacion
from .serializers import ReservaSerializer, PoliticaCancelacionSerializer
from apps.prestadores.mi_negocio.permissions import IsPrestadorOwner

class ReservaAdminViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        """
        El proveedor solo puede ver sus propias reservas.
        """
        return .objects.all()

    def perform_create(self, serializer):
        """
        Asigna el perfil del proveedor automáticamente al crear una reserva.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)

class PoliticaCancelacionAdminViewSet(viewsets.ModelViewSet):
    serializer_class = PoliticaCancelacionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        """
        El proveedor solo puede ver sus propias políticas de cancelación.
        """
        return .objects.all()

    def perform_create(self, serializer):
        """
        Asigna el perfil del proveedor automáticamente al crear una política.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)

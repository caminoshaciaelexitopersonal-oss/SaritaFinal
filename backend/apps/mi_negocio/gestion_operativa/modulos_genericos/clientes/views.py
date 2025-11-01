
from rest_framework import viewsets, permissions
from .models import Cliente
from .serializers import ClienteSerializer
from apps.mi_negocio.permissions import IsPrestadorOwner

class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los Clientes (CRM) de un Prestador.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        """
        Filtra el queryset para devolver solo los clientes
        asociados al perfil del prestador que realiza la solicitud.
        """
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return Cliente.objects.filter(perfil=user.perfil_prestador)
        # Si el usuario no es un prestador, no tiene acceso a ningún cliente.
        return Cliente.objects.none()

    def perform_create(self, serializer):
        """
        Asigna automáticamente el perfil del prestador al crear un nuevo cliente.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)

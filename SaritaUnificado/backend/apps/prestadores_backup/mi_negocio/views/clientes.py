from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from ..modelos.clientes import Cliente
from ..serializers.clientes import ClienteSerializer
from api.permissions import IsPrestador, IsPrestadorOwner

class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para la gestión de Clientes (CRM).
    """
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestador, IsPrestadorOwner]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'email', 'telefono']
    ordering_fields = ['nombre', 'fecha_creacion']

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Cliente.objects.filter(prestador=self.request.user.perfil_prestador)
        return Cliente.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)
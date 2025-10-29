# backend/apps/comercial/views.py
from rest_framework import viewsets, permissions
from .models import Cliente, FacturaVenta, PagoRecibido, NotaCredito
from .serializers import (
    ClienteSerializer,
    FacturaVentaSerializer,
    PagoRecibidoSerializer,
    NotaCreditoSerializer
)

class IsOwner(permissions.BasePermission):
    """
    Permiso para asegurar que el objeto pertenece al perfil del usuario.
    """
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint para la gestión de Clientes (CRM).
    """
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Filtra los clientes para que solo devuelva los del perfil del usuario logueado.
        """
        return Cliente.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        """
        Asigna el perfil del usuario logueado automáticamente al crear un cliente.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)


class FacturaVentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para la gestión de Facturas de Venta.
    """
    serializer_class = FacturaVentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Filtra las facturas para que solo devuelva las del perfil del usuario logueado.
        """
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador).select_related('cliente')

    def perform_create(self, serializer):
        """
        Asigna el perfil y el usuario creador automáticamente al crear una factura.
        """
        serializer.save(
            perfil=self.request.user.perfil_prestador,
            created_by=self.request.user
        )

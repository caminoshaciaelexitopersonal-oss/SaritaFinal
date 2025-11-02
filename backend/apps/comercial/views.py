from rest_framework import viewsets, permissions
from .models import Producto, FacturaVenta
from .serializers import (
    ProductoSerializer,
    FacturaVentaReadSerializer,
    FacturaVentaWriteSerializer,
)
from apps.mi_negocio.permissions import IsPrestadorOwner

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para los Productos y Servicios de un prestador.
    """
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return Producto.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class FacturaVentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para las Facturas de Venta de un prestador.
    """
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return FacturaVentaWriteSerializer
        return FacturaVentaReadSerializer

    def perform_create(self, serializer):
        # Lógica para calcular totales y crear items iría aquí o en un servicio.
        serializer.save(perfil=self.request.user.perfil_prestador)

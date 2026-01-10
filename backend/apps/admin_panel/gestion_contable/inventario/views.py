from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Almacen, MovimientoInventario
from .serializers import (
    AlmacenSerializer,
    MovimientoInventarioSerializer
)

        # La FK a producto ahora apunta a ProductoUnificado que tiene 'provider'
        if hasattr(obj, 'producto') and hasattr(obj.producto, 'provider'):
             return obj.producto.provider == request.user.perfil_prestador
        return False

class AlmacenAdminViewSet(viewsets.ModelViewSet):
    serializer_class = AlmacenSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return .objects.all()

class MovimientoInventarioAdminViewSet(viewsets.ModelViewSet):
    serializer_class = MovimientoInventarioSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        # Filtra movimientos basados en los productos del perfil del usuario
        return MovimientoInventario.objects.filter(producto__provider=self.request.user.perfil_prestador)

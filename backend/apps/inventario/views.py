# backend/apps/inventario/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Producto, MovimientoInventario
from .serializers import ProductoSerializer, MovimientoInventarioSerializer
from api.permissions import IsOwnerOrReadOnly

class ProductoViewSet(viewsets.ModelViewSet):
    """API para el CRUD de Productos."""
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

    @action(detail=True, methods=['get'])
    def kardex(self, request, pk=None):
        """Devuelve el historial de movimientos (Kardex) para un producto."""
        producto = self.get_object()
        movimientos = producto.movimientos.all().order_by('fecha', 'id')
        serializer = MovimientoInventarioSerializer(movimientos, many=True)
        return Response(serializer.data)

class MovimientoInventarioViewSet(viewsets.ReadOnlyModelViewSet):
    """API para consultar movimientos de inventario (Kardex)."""
    queryset = MovimientoInventario.objects.all()
    serializer_class = MovimientoInventarioSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filtra por productos que pertenecen al perfil del usuario
        return self.queryset.filter(producto__perfil=self.request.user.perfil_prestador)

from rest_framework import viewsets, permissions
from apps.admin_plataforma.gestion_contable.inventario.models import CategoriaProducto, Almacen, Producto, MovimientoInventario
from .serializers import (
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin
    CategoriaProductoSerializer,
    AlmacenSerializer,
    ProductoSerializer,
    MovimientoInventarioSerializer
)

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # El perfil está en el objeto directamente o a través de una relación
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'producto') and hasattr(obj.producto, 'perfil'):
             return obj.producto.perfil == request.user.perfil_prestador
        return False

class CategoriaProductoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CategoriaProductoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return CategoriaProducto.objects.filter(perfil=self.request.user.perfil_prestador)

class AlmacenViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = AlmacenSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return Almacen.objects.filter(perfil=self.request.user.perfil_prestador)

class ProductoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return Producto.objects.filter(perfil=self.request.user.perfil_prestador)

class MovimientoInventarioViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = MovimientoInventarioSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        # Filtra movimientos basados en los productos del perfil del usuario
        return MovimientoInventario.objects.filter(producto__perfil=self.request.user.perfil_prestador)

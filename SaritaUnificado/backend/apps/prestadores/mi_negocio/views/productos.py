from rest_framework import viewsets, permissions
from ..modelos.productos import Producto
from ..serializers.productos import ProductoSerializer
from api.permissions import IsPrestador, IsPrestadorOwner

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Producto.objects.filter(prestador=self.request.user.perfil_prestador)
        return Producto.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CategoriaMenu, ProductoMenu, Mesa, Pedido
from .serializers import CategoriaMenuSerializer, ProductoMenuSerializer, MesaSerializer, PedidoSerializer, CategoriaConProductosSerializer
from api.permissions import IsPrestador, IsPrestadorOwner

class CategoriaConProductosViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Vista de solo lectura para obtener las categorías con sus productos anidados.
    """
    serializer_class = CategoriaConProductosSerializer
    permission_classes = [IsAuthenticated, IsPrestador]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return CategoriaMenu.objects.filter(prestador=self.request.user.perfil_prestador).prefetch_related('productos')
        return CategoriaMenu.objects.none()

class CategoriaMenuViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaMenuSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return CategoriaMenu.objects.filter(prestador=self.request.user.perfil_prestador)
        return CategoriaMenu.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class ProductoMenuViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoMenuSerializer
    permission_classes = [IsAuthenticated, IsPrestador]

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return ProductoMenu.objects.all()

        if hasattr(self.request.user, 'perfil_prestador'):
             return ProductoMenu.objects.filter(categoria__prestador=self.request.user.perfil_prestador)
        return ProductoMenu.objects.none()

class MesaViewSet(viewsets.ModelViewSet):
    serializer_class = MesaSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Mesa.objects.filter(prestador=self.request.user.perfil_prestador)
        return Mesa.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, IsPrestador]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Pedido.objects.filter(mesa__prestador=self.request.user.perfil_prestador)
        return Pedido.objects.none()
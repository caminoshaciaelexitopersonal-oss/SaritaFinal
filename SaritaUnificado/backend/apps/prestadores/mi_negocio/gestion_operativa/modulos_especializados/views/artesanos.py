# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/views/artesanos.py
from ...modulos_genericos.views.base import GenericViewSet
from apps.prestadores.models import CategoriaProductoArtesanal, ProductoArtesanal, Pedido
from ..serializers.artesanos import CategoriaProductoArtesanalSerializer, ProductoArtesanalSerializer, PedidoSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

class CategoriaProductoArtesanalViewSet(ReadOnlyModelViewSet):
    queryset = CategoriaProductoArtesanal.objects.all()
    serializer_class = CategoriaProductoArtesanalSerializer

class ProductoArtesanalViewSet(GenericViewSet):
    queryset = ProductoArtesanal.objects.all()
    serializer_class = ProductoArtesanalSerializer

class PedidoViewSet(GenericViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

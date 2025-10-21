# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/productos_servicios.py
from .base import GenericViewSet
from apps.prestadores.models import ProductoServicio
from ..serializers.productos_servicios import ProductoServicioSerializer

class ProductoServicioViewSet(GenericViewSet):
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer

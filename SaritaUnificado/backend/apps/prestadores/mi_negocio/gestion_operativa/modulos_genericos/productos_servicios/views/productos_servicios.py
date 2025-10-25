# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/productos_servicios/views/productos_servicios.py
from ...views.base import GenericViewSet
from ..models.productos_servicios import ProductoServicio
from ..serializers.productos_servicios import ProductoServicioSerializer

class ProductoServicioViewSet(GenericViewSet):
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer

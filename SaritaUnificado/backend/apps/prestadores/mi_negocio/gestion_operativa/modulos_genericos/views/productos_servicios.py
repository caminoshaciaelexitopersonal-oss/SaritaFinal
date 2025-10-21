from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios import ProductoServicio
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.productos_servicios import ProductoServicioSerializer

class ProductoServicioViewSet(GenericViewSet):
    """
    API endpoint para gestionar los Productos y Servicios del prestador.
    """
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer

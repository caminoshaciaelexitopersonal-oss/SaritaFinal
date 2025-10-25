from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes import Cliente
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.clientes import ClienteSerializer

class ClienteViewSet(GenericViewSet):
    """
    API endpoint para gestionar los Clientes (CRM) del prestador.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

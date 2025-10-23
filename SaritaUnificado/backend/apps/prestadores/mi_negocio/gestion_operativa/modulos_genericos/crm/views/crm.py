# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/crm.py
from ...views.base import GenericViewSet
from ...models.crm import Cliente
from ..serializers.crm import ClienteSerializer

class ClienteViewSet(GenericViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

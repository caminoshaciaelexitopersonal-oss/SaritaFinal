from ...views.base import GenericViewSet
from ...inventario.models import Inventario
from ...inventario.serializers import InventarioSerializer

class InventarioViewSet(GenericViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

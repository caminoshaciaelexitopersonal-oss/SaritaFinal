from ...views.base import GenericViewSet
from ...costos.models import Costo
from ...costos.serializers import CostoSerializer

class CostoViewSet(GenericViewSet):
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer

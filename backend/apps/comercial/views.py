from rest_framework import viewsets
from .models import FacturaVenta
from .serializers import FacturaVentaSerializer # Necesitaré crear este serializador

class FacturaVentaViewSet(viewsets.ModelViewSet):
    queryset = FacturaVenta.objects.all()
    serializer_class = FacturaVentaSerializer

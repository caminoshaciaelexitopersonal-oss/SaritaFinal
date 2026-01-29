# from rest_framework import viewsets
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin
# from apps.admin_plataforma.gestion_contable.empresa.models import Inventario, Costo
# from .serializers import InventarioSerializer, CostoSerializer

# class InventarioViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
#     queryset = Inventario.objects.all()
#     serializer_class = InventarioSerializer

# class CostoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
#     queryset = Costo.objects.all()
#     serializer_class = CostoSerializer

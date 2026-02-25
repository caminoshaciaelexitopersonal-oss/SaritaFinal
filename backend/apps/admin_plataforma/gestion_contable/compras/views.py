from rest_framework import viewsets, permissions
from .models import Supplier, PurchaseInvoice
from .serializers import SupplierSerializer, PurchaseInvoiceSerializer
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

class SupplierViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class PurchaseInvoiceViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

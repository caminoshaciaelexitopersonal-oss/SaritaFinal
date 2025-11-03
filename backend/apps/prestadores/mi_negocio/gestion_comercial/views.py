from rest_framework import viewsets, permissions
from .models import FacturaVenta, ReciboCaja
from .serializers import FacturaVentaSerializer, ReciboCajaSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # El perfil está directamente en el objeto FacturaVenta o ReciboCaja.
        return obj.perfil == request.user.perfil_prestador

class FacturaVentaViewSet(viewsets.ModelViewSet):
    serializer_class = FacturaVentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador)

class ReciboCajaViewSet(viewsets.ModelViewSet):
    serializer_class = ReciboCajaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return ReciboCaja.objects.filter(perfil=self.request.user.perfil_prestador)

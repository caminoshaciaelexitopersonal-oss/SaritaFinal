from rest_framework import viewsets, permissions
from .models import CuentaBancaria, OrdenPago
from .serializers import CuentaBancariaSerializer, OrdenPagoSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return str(obj.perfil_ref_id) == str(request.user.perfil_prestador.id)

class CuentaBancariaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaBancariaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return CuentaBancaria.objects.filter(perfil_ref_id=self.request.user.perfil_prestador.id)
        return CuentaBancaria.objects.none()

class OrdenPagoViewSet(viewsets.ModelViewSet):
    serializer_class = OrdenPagoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return OrdenPago.objects.filter(perfil_ref_id=self.request.user.perfil_prestador.id)
        return OrdenPago.objects.none()

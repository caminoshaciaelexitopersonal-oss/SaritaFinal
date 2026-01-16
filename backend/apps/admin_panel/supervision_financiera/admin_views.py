from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_financiera.models import CuentaBancaria, OrdenPago
from .serializers import CuentaBancariaSerializer, OrdenPagoSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class CuentaBancariaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaBancariaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return CuentaBancaria.objects.filter(perfil=self.request.user.perfil_prestador)

class OrdenPagoViewSet(viewsets.ModelViewSet):
    serializer_class = OrdenPagoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return OrdenPago.objects.filter(perfil=self.request.user.perfil_prestador)

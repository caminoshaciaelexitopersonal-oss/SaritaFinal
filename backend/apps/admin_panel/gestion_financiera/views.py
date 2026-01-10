from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_financiera.models import CuentaBancaria, OrdenPago
from .admin_serializers import CuentaBancariaSerializer, OrdenPagoSerializer

# Vista para el Administrador General

class CuentaBancariaAdminViewSet(viewsets.ModelViewSet):
    """
    ViewSet para que el Administrador gestione Cuentas Bancarias de todos los prestadores.
    """
    serializer_class = CuentaBancariaSerializer
    permission_classes = [permissions.IsAdminUser] # Solo Admins

    def get_queryset(self):
        # El admin puede ver todas las cuentas bancarias
        return CuentaBancaria.objects.all()

class OrdenPagoAdminViewSet(viewsets.ModelViewSet):
    """
    ViewSet para que el Administrador gestione Órdenes de Pago de todos los prestadores.
    """
    serializer_class = OrdenPagoSerializer
    permission_classes = [permissions.IsAdminUser] # Solo Admins

    def get_queryset(self):
        # El admin puede ver todas las órdenes de pago
        return OrdenPago.objects.all()

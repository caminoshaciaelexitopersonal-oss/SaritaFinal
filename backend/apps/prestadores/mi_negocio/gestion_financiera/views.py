from django.db.models import Sum
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CuentaBancaria, TransaccionBancaria
# Corregir importaciones para apuntar a la estructura modular interna
from apps.prestadores.mi_negocio.gestion_comercial.models import FacturaVenta
from apps.prestadores.mi_negocio.gestion_contable.compras.models import FacturaCompra
from .serializers import CuentaBancariaSerializer, TransaccionBancariaSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'cuenta') and hasattr(obj.cuenta, 'perfil'):
             return obj.cuenta.perfil == request.user.perfil_prestador
        return False

class CuentaBancariaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaBancariaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return CuentaBancaria.objects.filter(perfil=self.request.user.perfil_prestador)

class TransaccionBancariaViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionBancariaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return TransaccionBancaria.objects.filter(cuenta__perfil=self.request.user.perfil_prestador)

class ReporteIngresosGastosView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        perfil = request.user.perfil_prestador

        # Obtener fechas del query string, con valores por defecto si no se proveen
        fecha_inicio = request.query_params.get('fecha_inicio', '2000-01-01')
        fecha_fin = request.query_params.get('fecha_fin', '2999-12-31')

        total_ingresos = FacturaVenta.objects.filter(
            perfil=perfil,
            fecha_emision__range=[fecha_inicio, fecha_fin],
            estado__in=[FacturaVenta.Estado.PAGADA, FacturaVenta.Estado.ENVIADA]
        ).aggregate(total=Sum('total'))['total'] or 0

        total_gastos = FacturaCompra.objects.filter(
            perfil=perfil,
            fecha_emision__range=[fecha_inicio, fecha_fin],
            estado__in=[FacturaCompra.Estado.PAGADA, FacturaCompra.Estado.POR_PAGAR]
        ).aggregate(total=Sum('total'))['total'] or 0

        data = {
            'total_ingresos': total_ingresos,
            'total_gastos': total_gastos,
            'neto': total_ingresos - total_gastos
        }
        return Response(data)

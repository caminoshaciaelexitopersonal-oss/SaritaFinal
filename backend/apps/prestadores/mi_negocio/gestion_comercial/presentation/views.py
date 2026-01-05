import logging
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from django.utils import timezone

logger = logging.getLogger(__name__)
from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal
from django.core.exceptions import ValidationError

from apps.prestadores.mi_negocio.gestion_financiera.models import TransaccionBancaria
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction as ContabTransaction, ChartOfAccount
from apps.prestadores.mi_negocio.gestion_contable.services import FacturaVentaAccountingService
from apps.prestadores.mi_negocio.gestion_contable.inventario.models import MovimientoInventario, Almacen
from .serializers import (
    FacturaVentaListSerializer,
    FacturaVentaDetailSerializer,
    ReciboCajaSerializer,
    OperacionComercialSerializer
)
from ..dian_services import DianService
from ..domain.models import OperacionComercial, FacturaVenta, ReciboCaja
from ..services import FacturacionService

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class OperacionComercialViewSet(viewsets.ModelViewSet):
    serializer_class = OperacionComercialSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return OperacionComercial.objects.filter(perfil=self.request.user.perfil_prestador)

    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        operacion = self.get_object()
        if operacion.estado != OperacionComercial.Estado.BORRADOR:
            return Response(
                {"error": "Solo se pueden confirmar operaciones en estado 'Borrador'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            FacturacionService.facturar_operacion_confirmada(operacion)
        except ValidationError as e:
            return Response({"error": "Error de validación durante la facturación.", "detalle": e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Error inesperado durante la facturación.", "detalle": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(OperacionComercialSerializer(operacion).data)


class FacturaVentaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_serializer_class(self):
        if self.action == 'list':
            return FacturaVentaListSerializer
        return FacturaVentaDetailSerializer

    def get_queryset(self):
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador).select_related('cliente')

    # La acción 'registrar-pago' y otras acciones específicas de la factura se mantienen.
    @action(detail=True, methods=['post'], url_path='registrar-pago')
    @transaction.atomic
    def registrar_pago(self, request, pk=None):
        factura = self.get_object()
        perfil = request.user.perfil_prestador
        # ... (lógica de registro de pago existente)
        monto_str = request.data.get('monto')
        cuenta_bancaria_id = request.data.get('cuenta_bancaria_id')

        if not monto_str or not cuenta_bancaria_id:
            return Response({"error": "Se requiere 'monto' y 'cuenta_bancaria_id'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            monto = Decimal(monto_str)
            cuenta_bancaria = CuentaBancaria.objects.get(id=cuenta_bancaria_id, perfil=perfil)
        except (ValueError, CuentaBancaria.DoesNotExist):
            return Response({"error": "Monto inválido o cuenta bancaria no encontrada."}, status=status.HTTP_400_BAD_REQUEST)

        recibo = ReciboCaja.objects.create(
            perfil=perfil,
            factura=factura,
            cuenta_bancaria=cuenta_bancaria,
            fecha_pago=request.data.get('fecha_pago'),
            monto=monto,
            metodo_pago=request.data.get('metodo_pago', 'TRANSFERENCIA')
        )
        factura.actualizar_estado_pago()
        return Response({"status": "Pago registrado con éxito"}, status=status.HTTP_200_OK)


class ReciboCajaViewSet(viewsets.ModelViewSet):
    serializer_class = ReciboCajaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return ReciboCaja.objects.filter(perfil=self.request.user.perfil_prestador)

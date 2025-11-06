from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal

from .models import FacturaVenta, ReciboCaja, CuentaBancaria
from .serializers import FacturaVentaSerializer, ReciboCajaSerializer
from apps.prestadores.mi_negocio.gestion_financiera.models import CashTransaction
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction as ContabTransaction, ChartOfAccount


class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class FacturaVentaViewSet(viewsets.ModelViewSet):
    serializer_class = FacturaVentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador)

    @action(detail=True, methods=['post'], url_path='registrar-pago')
    @transaction.atomic
    def registrar_pago(self, request, pk=None):
        factura = self.get_object()
        perfil = request.user.perfil_prestador
        monto_str = request.data.get('monto')
        cuenta_bancaria_id = request.data.get('cuenta_bancaria_id')

        if not monto_str or not cuenta_bancaria_id:
            return Response({"error": "Se requiere 'monto' y 'cuenta_bancaria_id'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            monto = Decimal(monto_str)
            cuenta_bancaria = CuentaBancaria.objects.get(id=cuenta_bancaria_id, perfil=perfil)
        except (ValueError, CuentaBancaria.DoesNotExist):
            return Response({"error": "Monto inválido o cuenta bancaria no encontrada."}, status=status.HTTP_400_BAD_REQUEST)

        # 1. Crear Recibo de Caja
        recibo = ReciboCaja.objects.create(
            perfil=perfil,
            factura=factura,
            cuenta_bancaria=cuenta_bancaria,
            fecha_pago=request.data.get('fecha_pago'),
            monto=monto,
            metodo_pago=request.data.get('metodo_pago', 'TRANSFERENCIA')
        )

        # 2. Crear Transacción de Tesorería
        CashTransaction.objects.create(
            perfil=perfil,
            bank_account=cuenta_bancaria,
            transaction_type='DEPOSIT',
            amount=monto,
            description=f"Pago de Factura No. {factura.numero_factura}"
        )

        # 3. Crear Asiento Contable del Pago
        try:
            cuenta_caja_bancos = cuenta_bancaria.chart_of_account
            cuenta_cxp = ChartOfAccount.objects.get(perfil=perfil, code='130505') # Cuentas por Cobrar
        except ChartOfAccount.DoesNotExist:
            return Response({"error": "Cuentas contables requeridas no encontradas."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=recibo.fecha_pago,
            description=f"Pago de Factura No. {factura.numero_factura}",
            entry_type="PAGO_RECIBIDO",
            user=request.user,
            origin_document=recibo
        )

        # Débito a Caja/Bancos
        ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_caja_bancos, debit=monto, credit=Decimal('0.00'))
        # Crédito a Cuentas por Cobrar
        ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_cxp, debit=Decimal('0.00'), credit=monto)

        factura.actualizar_estado_pago()

        return Response({"status": "Pago registrado con éxito"}, status=status.HTTP_200_OK)

class ReciboCajaViewSet(viewsets.ModelViewSet):
    serializer_class = ReciboCajaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return ReciboCaja.objects.filter(perfil=self.request.user.perfil_prestador)

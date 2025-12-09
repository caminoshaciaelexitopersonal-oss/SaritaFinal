from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal

from .models import FacturaVenta, ReciboCaja, CuentaBancaria
from .serializers import FacturaVentaSerializer, ReciboCajaSerializer
from apps.prestadores.mi_negocio.gestion_financiera.models import TransaccionBancaria
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction as ContabTransaction, ChartOfAccount
from apps.prestadores.mi_negocio.gestion_contable.inventario.models import MovimientoInventario, Almacen

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class FacturaVentaViewSet(viewsets.ModelViewSet):
    serializer_class = FacturaVentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        perfil = self.request.user.perfil_prestador
        with transaction.atomic():
            factura = serializer.save(perfil=perfil)

            # --- Creación del Asiento Contable de la Venta ---
            try:
                cuenta_ingresos = ChartOfAccount.objects.get(code__startswith='4135', perfil=perfil)
                cuenta_cxc = ChartOfAccount.objects.get(code__startswith='1305', perfil=perfil)
            except ChartOfAccount.DoesNotExist:
                # Si las cuentas no existen, no se puede crear el asiento.
                # En un entorno de producción, esto debería manejarse con una configuración más explícita.
                return

            journal_entry = JournalEntry.objects.create(
                perfil=perfil,
                entry_date=factura.fecha_emision,
                description=f"Venta según Factura No. {factura.numero_factura}",
                entry_type="VENTA",
                user=self.request.user,
                origin_document=factura
            )

            # Débito a Cuentas por Cobrar
            ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_cxc, debit=factura.total, credit=Decimal('0.00'))
            # Crédito a Ingresos
            ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_ingresos, debit=Decimal('0.00'), credit=factura.total)

            # --- Creación de Movimientos de Inventario ---
            try:
                # Asumimos un almacén principal. En un sistema real, esto sería seleccionable.
                almacen_principal = Almacen.objects.get(perfil=perfil, nombre__icontains='principal')
                for item in factura.items.all():
                    MovimientoInventario.objects.create(
                        producto=item.producto,
                        almacen=almacen_principal,
                        tipo_movimiento=MovimientoInventario.TipoMovimiento.SALIDA,
                        cantidad=item.cantidad,
                        descripcion=f"Venta según Factura No. {factura.numero_factura}",
                        usuario=self.request.user
                    )
            except Almacen.DoesNotExist:
                # Si no hay almacén principal, no se crean los movimientos.
                # Se podría registrar un log o una advertencia.
                pass


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
        TransaccionBancaria.objects.create(
            cuenta=cuenta_bancaria,
            fecha=recibo.fecha_pago,
            tipo='INGRESO',
            monto=monto,
            descripcion=f"Pago de Factura No. {factura.numero_factura}",
            creado_por=request.user
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

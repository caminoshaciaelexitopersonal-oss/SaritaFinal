# backend/apps/prestadores/mi_negocio/gestion_contable/services.py
from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError

from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta
from .contabilidad.models import JournalEntry, Transaction, ChartOfAccount

class FacturaVentaAccountingService:
    """
    Servicio encapsulado para manejar toda la lógica contable relacionada
    con las facturas de venta.
    """

    @staticmethod
    @transaction.atomic
    def registrar_factura_venta(factura: FacturaVenta):
        """
        Crea y valida el asiento contable para una factura de venta emitida.

        Este método es transaccional. Si alguna parte de la lógica contable falla,
        toda la operación se revierte.

        Args:
            factura: La instancia de FacturaVenta que se va a registrar.

        Raises:
            ValidationError: Si las cuentas contables no están configuradas,
                             o si el asiento resultante no cumple con la partida doble.
        """
        perfil = factura.perfil

        # 1. Obtener las cuentas contables requeridas
        try:
            cuenta_cxc = ChartOfAccount.objects.get(perfil=perfil, code='1305') # Cuentas por Cobrar
            cuenta_ingresos = ChartOfAccount.objects.get(perfil=perfil, code='4135') # Ingresos
            cuenta_iva = ChartOfAccount.objects.get(perfil=perfil, code='2408') # IVA por Pagar
        except ChartOfAccount.DoesNotExist as e:
            raise ValidationError(
                f"Configuración contable incompleta para el perfil {perfil.nombre_comercial}. "
                f"No se encontró una de las cuentas requeridas (1305, 4135, 2408). Detalle: {e}"
            )

        # 2. Crear el encabezado del asiento contable
        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=factura.fecha_emision,
            description=f"Venta según Factura No. {factura.numero_factura}",
            entry_type="VENTA",
            user=factura.creado_por,
            # TODO: Reactivar origin_document una vez que el entorno de pruebas maneje correctamente los GenericForeignKeys.
            # origin_document=factura
        )

        # 3. Crear las transacciones (líneas del asiento)
        # Débito a Cuentas por Cobrar por el total de la factura
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_cxc,
            debit=factura.total,
            credit=Decimal('0.00')
        )

        # Crédito a Ingresos por el subtotal
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_ingresos,
            debit=Decimal('0.00'),
            credit=factura.subtotal
        )

        # Crédito a IVA por Pagar (si hay impuestos)
        if factura.impuestos > 0:
            Transaction.objects.create(
                journal_entry=journal_entry,
                account=cuenta_iva,
                debit=Decimal('0.00'),
                credit=factura.impuestos
            )

        # 4. Validar la partida doble
        # El método clean() que añadimos se encarga de esto.
        journal_entry.clean()

        return journal_entry

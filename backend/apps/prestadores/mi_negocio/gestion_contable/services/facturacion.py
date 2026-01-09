# Este servicio contendrá la lógica contable para la facturación.
from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError

from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta
from ..contabilidad.models import JournalEntry, Transaction, ChartOfAccount

class FacturaVentaAccountingService:
    @staticmethod
    @transaction.atomic
    def registrar_factura_venta(factura: FacturaVenta, cliente, perfil):
        # El perfil ahora se pasa como un argumento resuelto para desacoplar el servicio.
        try:
            # CORRECCIÓN: Filtrar por `perfil_ref_id` en lugar de `perfil`.
            cuenta_cxc = ChartOfAccount.objects.get(perfil_ref_id=perfil.id, code='1305')
            cuenta_ingresos = ChartOfAccount.objects.get(perfil_ref_id=perfil.id, code='4135')
            cuenta_iva = ChartOfAccount.objects.get(perfil_ref_id=perfil.id, code='2408')
        except ChartOfAccount.DoesNotExist as e:
            raise ValidationError(f"Configuración contable incompleta. Detalle: {e}")

        # CORRECCIÓN: Los campos de auditoría y totales se obtienen de la operación.
        journal_entry = JournalEntry.objects.create(
            perfil_ref_id=perfil.id,
            entry_date=factura.fecha_emision,
            description=f"Venta según Factura No. {factura.numero_factura}",
            entry_type="VENTA",
            user=factura.operacion.creado_por,
        )

        # CORRECCIÓN: Los valores se obtienen de la operación asociada, no de la factura.
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_cxc, debit=factura.operacion.total)
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_ingresos, credit=factura.operacion.subtotal)
        if factura.operacion.impuestos > 0:
            Transaction.objects.create(journal_entry=journal_entry, account=cuenta_iva, credit=factura.operacion.impuestos)

        journal_entry.clean()
        return journal_entry

# Este servicio contendrá la lógica contable para la facturación.
from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError

from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta
from ..contabilidad.models import JournalEntry, Transaction, ChartOfAccount

class FacturaVentaAccountingService:
    @staticmethod
    @transaction.atomic
    def registrar_factura_venta(factura: FacturaVenta):
        perfil = factura.perfil
        try:
            cuenta_cxc = ChartOfAccount.objects.get(perfil=perfil, code='1305')
            cuenta_ingresos = ChartOfAccount.objects.get(perfil=perfil, code='4135')
            cuenta_iva = ChartOfAccount.objects.get(perfil=perfil, code='2408')
        except ChartOfAccount.DoesNotExist as e:
            raise ValidationError(f"Configuración contable incompleta. Detalle: {e}")

        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=factura.fecha_emision,
            description=f"Venta según Factura No. {factura.numero_factura}",
            entry_type="VENTA",
            user=factura.creado_por,
        )

        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_cxc, debit=factura.total)
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_ingresos, credit=factura.subtotal)
        if factura.impuestos > 0:
            Transaction.objects.create(journal_entry=journal_entry, account=cuenta_iva, credit=factura.impuestos)

        journal_entry.clean()
        return journal_entry

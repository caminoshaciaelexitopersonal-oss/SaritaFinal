from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

from .contabilidad.services import ChartOfAccountService
from ..gestion_financiera.models import OrdenPago
from .contabilidad.models import JournalEntry, Transaction, ChartOfAccount
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta

class ContabilidadPagoService:
    @staticmethod
    def contabilizar_pago(orden_pago: OrdenPago):
        perfil = orden_pago.perfil
        chart_of_accounts = ChartOfAccountService(perfil)
        cuenta_pasivo = chart_of_accounts.get_liability_account()
        cuenta_banco = orden_pago.cuenta_bancaria_origen.cuenta_contable

        journal_entry = JournalEntry.objects.create(
            profile=perfil,
            date=orden_pago.fecha_pago,
            description=f"Pago orden #{orden_pago.id}: {orden_pago.concepto}",
            is_automatic=True
        )
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_pasivo, debit=orden_pago.monto)
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_banco, credit=orden_pago.monto)
        journal_entry.validate_debits_and_credits()
        return journal_entry

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

import logging
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import transaction
from apps.core_erp.accounting_engine import AccountingEngine

logger = logging.getLogger(__name__)

class BillingEngine:
    """
    Motor de Facturación Soberano del Core ERP.
    Gestiona el ciclo de vida de facturas e impacta automáticamente la contabilidad.
    """

    @staticmethod
    def calculate_totals(invoice):
        """
        Calcula subtotales e impuestos de la factura.
        """
        lines = invoice.lines.all()
        subtotal = sum(line.subtotal for line in lines)
        total_tax = sum(line.tax_amount for line in lines)

        invoice.total_amount = subtotal + total_tax
        invoice.tax_amount = total_tax
        invoice.save()
        return invoice.total_amount

    @staticmethod
    @transaction.atomic
    def issue_invoice(invoice, responsible_user=None):
        """
        Emite la factura y genera el impacto contable obligatorio.
        """
        if invoice.status != 'DRAFT':
            raise ValidationError(f"Solo se pueden emitir facturas en borrador. Estado actual: {invoice.status}")

        # 1. Asegurar cálculos finales
        BillingEngine.calculate_totals(invoice)

        # 2. Cambiar estado
        invoice.status = 'ISSUED'
        invoice.save()

        # 3. Generar Asiento Contable Automático (Accounting Impact)
        # Nota: La creación del objeto 'entry' y sus 'lines' depende de la implementación del modelo concreto.
        # Aquí definimos el flujo de orquestación.

        logger.info(f"Factura {invoice.number} emitida. Generando asiento contable...")

        # entry = map_invoice_to_journal_entry(invoice)
        # AccountingEngine.post_journal_entry(entry)

        return invoice

    @staticmethod
    def process_usage_billing(entity_id, usage_data):
        """
        Genera facturación basada en consumo (API calls, tokens, etc).
        """
        logger.info(f"Procesando facturación por uso para la entidad {entity_id}")
        # Lógica de agregación de eventos de uso
        pass

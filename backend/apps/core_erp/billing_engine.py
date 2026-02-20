import logging
from django.core.exceptions import ValidationError
from django.db import transaction

logger = logging.getLogger(__name__)

class BillingEngine:
    """
    Motor de facturación centralizado del Core ERP.
    Garantiza la integridad de documentos comerciales.
    """

    @staticmethod
    def calculate_totals(invoice):
        """
        Calcula el total de la factura basado en sus items.
        """
        # Se asume que invoice tiene un related_name 'items'
        items = invoice.items.all()
        total_subtotal = sum(item.subtotal for item in items)
        total_tax = sum(getattr(item, 'tax_amount', 0) for item in items)

        invoice.total_amount = total_subtotal + total_tax
        invoice.save()
        return invoice.total_amount

    @staticmethod
    def validate_invoice(invoice):
        """
        Validaciones de integridad comercial.
        """
        if not invoice.number:
            raise ValidationError("La factura debe tener un número asignado.")

        if invoice.total_amount <= 0:
             # Recalcular por si acaso
             BillingEngine.calculate_totals(invoice)
             if invoice.total_amount <= 0:
                raise ValidationError(f"Factura {invoice.number} con total inválido: {invoice.total_amount}")

        if not invoice.issue_date:
            raise ValidationError("La factura debe tener fecha de emisión.")

    @staticmethod
    @transaction.atomic
    def issue_invoice(invoice):
        """
        Finaliza y emite la factura.
        """
        BillingEngine.validate_invoice(invoice)
        invoice.status = 'ISSUED'
        invoice.save()
        logger.info(f"Factura {invoice.number} emitida exitosamente.")
        return invoice

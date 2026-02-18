from django.core.exceptions import ValidationError

class BillingEngine:
    """
    Motor de facturación centralizado.
    """

    @staticmethod
    def calculate_totals(invoice):
        """
        Calcula el total de la factura basado en sus items.
        """
        items = invoice.items.all()
        total = sum(item.subtotal for item in items)
        invoice.total_amount = total
        invoice.save()
        return total

    @staticmethod
    def validate_invoice(invoice):
        if not invoice.number:
            raise ValidationError("La factura debe tener un número.")
        if invoice.total_amount <= 0:
            raise ValidationError("El total de la factura debe ser mayor a cero.")

from decimal import Decimal
from django.core.exceptions import ValidationError

class TaxEngine:
    """
    Motor fiscal centralizado para cálculo de impuestos y retenciones.
    """

    @staticmethod
    def calculate_tax(base_amount, tax_rate_percentage):
        """
        Calcula el valor del impuesto sobre una base.
        """
        if tax_rate_percentage < 0:
            raise ValidationError("La tasa de impuesto no puede ser negativa.")

        return (base_amount * Decimal(str(tax_rate_percentage)) / Decimal('100')).quantize(Decimal('0.01'))

    @staticmethod
    def calculate_retention(base_amount, retention_rate_percentage):
        """
        Calcula el valor de la retención.
        """
        return (base_amount * Decimal(str(retention_rate_percentage)) / Decimal('100')).quantize(Decimal('0.01'))

    @staticmethod
    def apply_tax_to_invoice_item(item, tax_rate):
        """
        Aplica impuesto a un item de factura.
        """
        item.tax_amount = TaxEngine.calculate_tax(item.subtotal, tax_rate)
        item.total_amount = item.subtotal + item.tax_amount
        item.save()
        return item.total_amount

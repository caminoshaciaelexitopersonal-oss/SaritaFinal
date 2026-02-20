from django.core.exceptions import ValidationError

from django.utils import timezone
from .models import Invoice, InvoiceItem

class BillingEngine:
    """
    Motor de facturación centralizado.
    """

    @staticmethod
    def create_invoice(company, invoice_data):
        """
        Crea una factura para una empresa.
        """
        invoice = Invoice.objects.create(
            client_id=company.id,
            number=f"INV-{timezone.now().strftime('%Y%m%d%H%M%S')}",
            issue_date=timezone.now().date(),
            due_date=(timezone.now() + timezone.timedelta(days=30)).date(),
            status='PENDING'
        )

        InvoiceItem.objects.create(
            invoice=invoice,
            description=invoice_data['concept'],
            quantity=1,
            unit_price=invoice_data['amount'],
            subtotal=invoice_data['amount']
        )

        BillingEngine.calculate_totals(invoice)
        BillingEngine.validate_invoice(invoice)

        return invoice

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

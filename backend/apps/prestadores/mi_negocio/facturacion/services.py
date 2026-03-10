import logging
import uuid
from django.db import transaction
from django.utils import timezone
from .models import Factura

logger = logging.getLogger(__name__)

class InvoicingService:
    @staticmethod
    def generate_invoice_number(provider):
        """
        Genera numeración secuencial: FAC-YYYY-XXXXX
        """
        year = timezone.now().year
        last_invoice = Factura.objects.filter(
            provider=provider,
            numero_factura__startswith=f"FAC-{year}"
        ).order_by('-numero_factura').first()

        if last_invoice:
            last_number = int(last_invoice.numero_factura.split('-')[-1])
            new_number = last_number + 1
        else:
            new_number = 1

        return f"FAC-{year}-{str(new_number).zfill(5)}"

    @staticmethod
    @transaction.atomic
    def generate_invoice(venta):
        """
        Crea la factura formal asociada a una venta confirmada.
        """
        if hasattr(venta, 'factura'):
            return venta.factura

        num_factura = InvoicingService.generate_invoice_number(venta.provider)

        # Simulación de firma digital / CUFE para Fase 2
        cufe_simulado = f"CUFE-{uuid.uuid4().hex[:32].upper()}"

        factura = Factura.objects.create(
            provider=venta.provider,
            venta=venta,
            numero_factura=num_factura,
            total=venta.total,
            estado=Factura.Estado.EMITIDA,
            cufe=cufe_simulado
        )

        logger.info(f"Factura generada: {num_factura} para Venta {venta.id}")
        return factura

# backend/apps/comercial/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FacturaVenta, PagoRecibido
from apps.contabilidad.services import create_full_journal_entry

@receiver(post_save, sender=FacturaVenta)
def contabilizar_factura_venta(sender, instance, created, **kwargs):
    if created and instance.estado == 'EMITIDA':
        # ... (lógica original)
        pass

@receiver(post_save, sender=PagoRecibido)
def procesar_pago_recibido(sender, instance, created, **kwargs):
    if created:
        # ... (lógica original)
        pass

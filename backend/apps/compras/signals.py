# backend/apps/compras/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FacturaProveedor, PagoRealizado
from apps.contabilidad.services import create_full_journal_entry

@receiver(post_save, sender=FacturaProveedor)
def contabilizar_factura_proveedor(sender, instance, created, **kwargs):
    if created and instance.estado == 'PENDIENTE':
        try:
            # ... (lógica de contabilización)
            user = instance.perfil.usuario
            transactions_data = [
                {'account_code': '5105', 'debit': instance.total, 'credit': 0},
                {'account_code': '2205', 'debit': 0, 'credit': instance.total}
            ]
            create_full_journal_entry(
                user=user, perfil=instance.perfil, entry_date=instance.fecha_emision,
                description=f"Contabilización de factura de proveedor #{instance.id}",
                entry_type='FP', transactions_data=transactions_data, origin_document=instance
            )
        except Exception as e:
            print(f"Error al contabilizar factura de proveedor {instance.id}: {e}")

@receiver(post_save, sender=PagoRealizado)
def procesar_pago_realizado(sender, instance, created, **kwargs):
    if created:
        factura = instance.factura
        factura.estado = 'PAGADA'
        factura.save()
        try:
            user = factura.perfil.usuario
            transactions_data = [
                {'account_code': '2205', 'debit': instance.monto, 'credit': 0},
                {'account_code': '110505', 'debit': 0, 'credit': instance.monto}
            ]
            create_full_journal_entry(
                user=user, perfil=instance.perfil, entry_date=instance.fecha_pago,
                description=f"Registro de pago para factura de proveedor #{factura.id}",
                entry_type='PP', transactions_data=transactions_data, origin_document=instance
            )
        except Exception as e:
            print(f"Error al contabilizar pago realizado {instance.id}: {e}")

# backend/apps/compras/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FacturaProveedor, PagoRealizado
from apps.contabilidad.services import create_full_journal_entry
from apps.inventario.services import registrar_entrada_inventario

@receiver(post_save, sender=FacturaProveedor)
def procesar_factura_proveedor(sender, instance, created, **kwargs):
    if created and instance.estado == 'PENDIENTE':
        # 1. Contabilización
        try:
            user = instance.perfil.usuario
            transactions_data = [
                {'account_code': '5105', 'debit': instance.total, 'credit': 0},
                {'account_code': '2205', 'debit': 0, 'credit': instance.total}
            ]
            create_full_journal_entry(
                user=user, perfil=instance.perfil, entry_date=instance.fecha_emision,
                description=f"Contabilización F.P. #{instance.id}",
                entry_type='FP', transactions_data=transactions_data, origin_document=instance
            )
        except Exception as e:
            print(f"Error al contabilizar factura proveedor {instance.id}: {e}")

        # 2. Registrar entrada de inventario
        try:
            registrar_entrada_inventario(factura=instance)
        except Exception as e:
            print(f"Error al registrar entrada de inventario para factura {instance.id}: {e}")

@receiver(post_save, sender=PagoRealizado)
def procesar_pago_realizado(sender, instance, created, **kwargs):
    if created:
        pass # Lógica de pago

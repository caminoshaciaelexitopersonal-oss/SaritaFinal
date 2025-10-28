# backend/apps/comercial/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FacturaVenta, PagoRecibido
from apps.contabilidad.services import create_full_journal_entry
from apps.inventario.services import registrar_salida_inventario

@receiver(post_save, sender=FacturaVenta)
def procesar_factura_venta(sender, instance, created, **kwargs):
    if created and instance.estado == 'EMITIDA':
        # 1. Contabilización del Ingreso
        try:
            transactions_data = [
                {'account_code': '130505', 'debit': instance.total, 'credit': 0},
                {'account_code': '4135', 'debit': 0, 'credit': instance.subtotal},
                {'account_code': '2408', 'debit': 0, 'credit': instance.impuestos}
            ]
            create_full_journal_entry(
                user=instance.created_by, perfil=instance.perfil, entry_date=instance.fecha_emision,
                description=f"Contabilización F.V. #{instance.id}",
                entry_type='FV', transactions_data=transactions_data, origin_document=instance
            )
        except Exception as e:
            print(f"Error al contabilizar ingreso de F.V. {instance.id}: {e}")

        # 2. Registrar salida de inventario
        try:
            registrar_salida_inventario(factura=instance)
        except Exception as e:
            print(f"Error al registrar salida de inventario para F.V. {instance.id}: {e}")
            return

        # 3. Contabilización del Costo de Venta (COGS)
        try:
            costo_total_salida = sum(item.cantidad * item.producto.costo_promedio_ponderado for item in instance.items.all())
            if costo_total_salida > 0:
                transactions_data = [
                    {'account_code': '6135', 'debit': costo_total_salida, 'credit': 0},
                    {'account_code': '1435', 'debit': 0, 'credit': costo_total_salida}
                ]
                create_full_journal_entry(
                    user=instance.created_by, perfil=instance.perfil, entry_date=instance.fecha_emision,
                    description=f"Costo de venta para F.V. #{instance.id}",
                    entry_type='COGS', transactions_data=transactions_data
                )
        except Exception as e:
            print(f"Error al contabilizar COGS para F.V. {instance.id}: {e}")

# ... (señal de pago sin cambios) ...
@receiver(post_save, sender=PagoRecibido)
def procesar_pago_recibido(sender, instance, created, **kwargs):
    if created:
        pass # Lógica de pago

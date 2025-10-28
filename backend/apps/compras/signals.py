# backend/apps/compras/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FacturaProveedor
from apps.contabilidad.services import create_full_journal_entry

@receiver(post_save, sender=FacturaProveedor)
def contabilizar_factura_proveedor(sender, instance, created, **kwargs):
    """
    Crea automáticamente el asiento contable al crear una nueva factura de proveedor.
    """
    if created and instance.estado == 'PENDIENTE':
        try:
            # NOTA: Los códigos de cuenta ('5105', '2205') son ejemplos.
            transactions_data = [
                {
                    'account_code': '5105', # Gastos (ej. Compras)
                    'debit': instance.total,
                    'credit': 0
                },
                {
                    'account_code': '2205', # Cuentas por Pagar Proveedores
                    'debit': 0,
                    'credit': instance.total
                }
            ]

            create_full_journal_entry(
                user=instance.created_by,
                perfil=instance.perfil,
                entry_date=instance.fecha_emision,
                description=f"Contabilización de factura de proveedor #{instance.id} de {instance.proveedor.nombre}",
                entry_type='FP', # Factura de Proveedor
                transactions_data=transactions_data,
                origin_document=instance
            )
        except Exception as e:
            print(f"Error al contabilizar factura de proveedor {instance.id}: {e}")

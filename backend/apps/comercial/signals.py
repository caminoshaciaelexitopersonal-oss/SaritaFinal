# backend/apps/comercial/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FacturaVenta
from apps.contabilidad.services import create_full_journal_entry

@receiver(post_save, sender=FacturaVenta)
def contabilizar_factura_venta(sender, instance, created, **kwargs):
    """
    Crea automáticamente el asiento contable al crear una nueva factura de venta.
    """
    if created and instance.estado == 'EMITIDA': # Solo al crear y si está emitida
        try:
            # NOTA: Los códigos de cuenta ('130505', '4135') son ejemplos.
            # Una implementación real los obtendría de una configuración contable.
            transactions_data = [
                {
                    'account_code': '130505', # Cuentas por Cobrar Clientes Nacionales
                    'debit': instance.total,
                    'credit': 0
                },
                {
                    'account_code': '4135', # Ingresos por Servicios
                    'debit': 0,
                    'credit': instance.subtotal
                },
                {
                    'account_code': '2408', # IVA Generado
                    'debit': 0,
                    'credit': instance.impuestos
                }
            ]

            create_full_journal_entry(
                user=instance.created_by,
                perfil=instance.perfil,
                entry_date=instance.fecha_emision,
                description=f"Contabilización de factura de venta #{instance.id} a {instance.cliente.nombre}",
                entry_type='FV', # Factura de Venta
                transactions_data=transactions_data,
                origin_document=instance
            )
        except Exception as e:
            # Manejar el error, por ejemplo, loggearlo.
            # Es importante que un fallo en la contabilización no detenga el flujo principal.
            print(f"Error al contabilizar factura de venta {instance.id}: {e}")

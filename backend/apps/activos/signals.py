# backend/apps/activos/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RegistroDepreciacion
from apps.contabilidad.services import create_full_journal_entry

@receiver(post_save, sender=RegistroDepreciacion)
def contabilizar_depreciacion(sender, instance, created, **kwargs):
    if created:
        try:
            activo = instance.activo
            # Cuentas de ejemplo
            transactions_data = [
                {'account_code': '5160', 'debit': instance.monto, 'credit': 0}, # Gasto Depreciación
                {'account_code': '1592', 'debit': 0, 'credit': instance.monto}  # Depreciación Acumulada
            ]
            create_full_journal_entry(
                user=activo.perfil.usuario,
                perfil=activo.perfil,
                entry_date=instance.fecha,
                description=f"Depreciación mensual de {activo.nombre}",
                entry_type='DEP',
                transactions_data=transactions_data,
                origin_document=instance
            )
        except Exception as e:
            print(f"Error al contabilizar depreciación {instance.id}: {e}")

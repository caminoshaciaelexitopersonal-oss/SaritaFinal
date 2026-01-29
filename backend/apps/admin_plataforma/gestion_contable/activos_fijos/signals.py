# backend/apps/prestadores/mi_negocio/gestion_contable/activos_fijos/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

from .models import CalculoDepreciacion
from apps.admin_plataforma.gestion_contable.contabilidad.models import JournalEntry, Transaction, ChartOfAccount

@receiver(post_save, sender=CalculoDepreciacion)
def crear_asiento_contable_depreciacion(sender, instance, created, **kwargs):
    if created:
        perfil = instance.activo.perfil

        try:
            # Estos códigos de cuenta son estándar, pero deberían ser configurables en un sistema real
            cuenta_gasto_dep = ChartOfAccount.objects.get(perfil=perfil, code='5160') # Gasto - Depreciaciones
            cuenta_dep_acum = ChartOfAccount.objects.get(perfil=perfil, code='1592') # Activo (Crédito) - Depreciación Acumulada
        except ChartOfAccount.DoesNotExist:
            return

        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=instance.fecha,
            description=f"Depreciación de {instance.activo.nombre} para el periodo.",
            entry_type="DEPRECIACION",
            user=instance.creado_por,
            origin_document=instance
        )

        # Débito al gasto de depreciación
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_gasto_dep,
            debit=instance.monto,
            credit=Decimal('0.00')
        )

        # Crédito a la depreciación acumulada
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_dep_acum,
            debit=Decimal('0.00'),
            credit=instance.monto
        )

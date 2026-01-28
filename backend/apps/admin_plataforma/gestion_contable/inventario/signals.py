# backend/apps/prestadores/mi_negocio/gestion_contable/inventario/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

from .models import MovimientoInventario
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction, ChartOfAccount

@receiver(post_save, sender=MovimientoInventario)
def crear_asiento_contable_movimiento_inventario(sender, instance, created, **kwargs):
    if created:
        perfil = instance.producto.perfil
        valor_movimiento = instance.cantidad * instance.producto.costo

        if valor_movimiento <= 0:
            return # No crear asientos para movimientos sin valor

        try:
            cuenta_inventario = ChartOfAccount.objects.get(perfil=perfil, code='1435') # Activo - Inventarios
            cuenta_cmv = ChartOfAccount.objects.get(perfil=perfil, code='6135') # Costo - Costo de Ventas
        except ChartOfAccount.DoesNotExist:
            # Si las cuentas no existen, no se puede crear el asiento.
            return

        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=instance.fecha.date(),
            description=f"Movimiento de inventario: {instance.get_tipo_movimiento_display()} de {instance.producto.nombre}",
            entry_type="INVENTARIO",
            user=instance.usuario,
            origin_document=instance
        )

        if instance.tipo_movimiento in [MovimientoInventario.TipoMovimiento.ENTRADA, MovimientoInventario.TipoMovimiento.AJUSTE_POSITIVO]:
            # Aumento de inventario: Débito a Inventario, Crédito a CMV
            Transaction.objects.create(
                journal_entry=journal_entry,
                account=cuenta_inventario,
                debit=valor_movimiento,
                credit=Decimal('0.00')
            )
            Transaction.objects.create(
                journal_entry=journal_entry,
                account=cuenta_cmv,
                debit=Decimal('0.00'),
                credit=valor_movimiento
            )
        elif instance.tipo_movimiento in [MovimientoInventario.TipoMovimiento.SALIDA, MovimientoInventario.TipoMovimiento.AJUSTE_NEGATIVO]:
            # Disminución de inventario: Débito a CMV, Crédito a Inventario
            Transaction.objects.create(
                journal_entry=journal_entry,
                account=cuenta_cmv,
                debit=valor_movimiento,
                credit=Decimal('0.00')
            )
            Transaction.objects.create(
                journal_entry=journal_entry,
                account=cuenta_inventario,
                debit=Decimal('0.00'),
                credit=valor_movimiento
            )

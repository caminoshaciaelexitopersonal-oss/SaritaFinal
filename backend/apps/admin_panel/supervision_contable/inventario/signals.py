# backend/apps/prestadores/mi_negocio/gestion_contable/inventario/signals.py
from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from decimal import Decimal

from .models import MovimientoInventario
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction, ChartOfAccount

@receiver(post_save, sender=MovimientoInventario)
def actualizar_stock_y_contabilidad_on_save(sender, instance, created, **kwargs):
    """
    Actualiza el stock del producto y crea el asiento contable correspondiente
    después de que se guarda un MovimientoInventario.
    """
    if not created:
        # Por ahora, no manejamos la edición de movimientos existentes para evitar complejidad.
        # Una implementación completa requeriría revertir el movimiento antiguo y aplicar el nuevo.
        return

    # --- 1. Actualización de Stock (Nueva Lógica) ---
    producto = instance.producto
    if producto.es_inventariable:
        # Usamos transaction.on_commit para asegurar que la actualización del stock
        # ocurra solo si la transacción principal (que guarda el movimiento) tiene éxito.
        def update_stock():
            if instance.tipo_movimiento in [
                MovimientoInventario.TipoMovimiento.ENTRADA,
                MovimientoInventario.TipoMovimiento.AJUSTE_POSITIVO,
            ]:
                producto.stock = F('stock') + instance.cantidad
            elif instance.tipo_movimiento in [
                MovimientoInventario.TipoMovimiento.SALIDA,
                MovimientoInventario.TipoMovimiento.AJUSTE_NEGATIVO,
            ]:
                producto.stock = F('stock') - instance.cantidad
            producto.save(update_fields=['stock'])

        transaction.on_commit(update_stock)


    # --- 2. Creación del Asiento Contable (Lógica Existente) ---
    perfil = instance.producto.provider
    costo = instance.producto.base_price.amount if instance.producto.base_price else Decimal('0.00')
    valor_movimiento = instance.cantidad * costo

    if valor_movimiento <= 0:
        return # No crear asientos para movimientos sin valor

    try:
        cuenta_inventario = ChartOfAccount.objects.get(perfil=perfil, code='1435') # Activo - Inventarios
        cuenta_cmv = ChartOfAccount.objects.get(perfil=perfil, code='6135') # Costo - Costo de Ventas
    except ChartOfAccount.DoesNotExist:
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
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_inventario, debit=valor_movimiento, credit=Decimal('0.00'))
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_cmv, debit=Decimal('0.00'), credit=valor_movimiento)
    elif instance.tipo_movimiento in [MovimientoInventario.TipoMovimiento.SALIDA, MovimientoInventario.TipoMovimiento.AJUSTE_NEGATIVO]:
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_cmv, debit=valor_movimiento, credit=Decimal('0.00'))
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_inventario, debit=Decimal('0.00'), credit=valor_movimiento)


@receiver(post_delete, sender=MovimientoInventario)
def actualizar_stock_on_delete(sender, instance, **kwargs):
    """
    Revierte la actualización de stock cuando se elimina un MovimientoInventario.
    """
    producto = instance.producto
    if producto.es_inventariable:
        # Usamos transaction.on_commit para la consistencia
        def revert_stock_update():
            if instance.tipo_movimiento in [
                MovimientoInventario.TipoMovimiento.ENTRADA,
                MovimientoInventario.TipoMovimiento.AJUSTE_POSITIVO,
            ]:
                # Si se elimina una entrada, el stock disminuye
                producto.stock = F('stock') - instance.cantidad
            elif instance.tipo_movimiento in [
                MovimientoInventario.TipoMovimiento.SALIDA,
                MovimientoInventario.TipoMovimiento.AJUSTE_NEGATIVO,
            ]:
                # Si se elimina una salida, el stock aumenta
                producto.stock = F('stock') + instance.cantidad
            producto.save(update_fields=['stock'])

        transaction.on_commit(revert_stock_update)

    # Nota: No se revierte el asiento contable al eliminar para mantener un rastro de auditoría.
    # Una implementación más avanzada podría crear un asiento contable de anulación.

# backend/apps/prestadores/mi_negocio/gestion_comercial/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

from .models import FacturaVenta
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction, ChartOfAccount

@receiver(post_save, sender=FacturaVenta)
def crear_asiento_contable_factura_venta(sender, instance, created, **kwargs):
    """
    Crea automáticamente el asiento contable cuando se crea una nueva factura de venta.
    """
    if created and instance.estado != FacturaVenta.Estado.BORRADOR:
        perfil = instance.perfil

        try:
            # Códigos de cuentas estándar
            cuenta_cxp = ChartOfAccount.objects.get(perfil=perfil, code='130505') # Activo - Cuentas por Cobrar Clientes
            cuenta_ingresos = ChartOfAccount.objects.get(perfil=perfil, code='4135') # Ingreso - Ingresos Operacionales
            cuenta_impuestos = ChartOfAccount.objects.get(perfil=perfil, code='2408') # Pasivo - IVA por Pagar
        except ChartOfAccount.DoesNotExist:
            # Si alguna cuenta esencial no existe, no se puede crear el asiento.
            # Se podría loggear un error aquí.
            return

        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=instance.fecha_emision,
            description=f"Asiento de venta por Factura No. {instance.numero_factura} a {instance.cliente.nombre}",
            entry_type="VENTA",
            user=instance.creado_por,
            origin_document=instance
        )

        # 1. Débito a Cuentas por Cobrar por el total de la factura
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_cxp,
            debit=instance.total,
            credit=Decimal('0.00')
        )

        # 2. Crédito a Ingresos por el subtotal
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_ingresos,
            debit=Decimal('0.00'),
            credit=instance.subtotal
        )

        # 3. Crédito a Impuestos por Pagar si hay impuestos
        if instance.impuestos > 0:
            Transaction.objects.create(
                journal_entry=journal_entry,
                account=cuenta_impuestos,
                debit=Decimal('0.00'),
                credit=instance.impuestos
            )

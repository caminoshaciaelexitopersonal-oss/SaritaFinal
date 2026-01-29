# backend/apps/prestadores/mi_negocio/gestion_contable/compras/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

from .models import FacturaCompra
from apps.admin_plataforma.gestion_contable.contabilidad.models import JournalEntry, Transaction, ChartOfAccount

@receiver(post_save, sender=FacturaCompra)
def crear_asiento_contable_factura_compra(sender, instance, created, **kwargs):
    """
    Crea automáticamente el asiento contable cuando se crea una nueva Factura de Compra.
    """
    if created:
        # Asumimos códigos de cuenta estándar. En un sistema real, esto sería configurable.
        # Por ejemplo, una cuenta de 'Cuentas por Pagar Proveedores' y una de 'Gastos Generales'.
        try:
            cuenta_por_pagar_code = '210501' # Pasivo - Cuentas por Pagar Nacionales
            cuenta_gasto_code = '510506'    # Gasto - Sueldos y Salarios (Ejemplo, debería ser una cuenta de compra/gasto)

            cuenta_por_pagar = ChartOfAccount.objects.get(code=cuenta_por_pagar_code)
            cuenta_gasto = ChartOfAccount.objects.get(code=cuenta_gasto_code)
        except ChartOfAccount.DoesNotExist:
            # Si las cuentas no existen, no podemos crear el asiento.
            # En un entorno real, esto debería registrar un error.
            return

        # 1. Crear la cabecera del asiento contable
        journal_entry = JournalEntry.objects.create(
            perfil=instance.perfil,
            entry_date=instance.fecha_emision,
            description=f"Asiento automático por Factura de Compra #{instance.numero_factura} de {instance.proveedor.nombre}",
            entry_type="COMPRA",
            user=instance.creado_por,
            origin_document=instance
        )

        # 2. Crear las transacciones de débito y crédito
        # Crédito a la cuenta por pagar (aumenta el pasivo)
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_por_pagar,
            credit=instance.total,
            debit=Decimal('0.00')
        )

        # Débito a la cuenta de gasto (aumenta el gasto)
        Transaction.objects.create(
            journal_entry=journal_entry,
            account=cuenta_gasto,
            debit=instance.total,
            credit=Decimal('0.00')
        )

import logging
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone
from .models import Account, JournalEntry, Transaction, FiscalPeriod

logger = logging.getLogger(__name__)

class AccountingEngine:
    """
    Motor contable centralizado para validación y procesamiento de asientos.
    """

    @staticmethod
    def validate_balance(entry):
        """
        Valida que un asiento esté balanceado (Debe = Haber).
        """
        # Usamos el related_name 'transactions' estandarizado
        transactions = entry.transactions.all()
        total_debit = sum(t.debit for t in transactions)
        total_credit = sum(t.credit for t in transactions)

        if total_debit != total_credit:
             raise ValidationError(f"Asiento descuadrado: Débito ({total_debit}) != Crédito ({total_credit})")

        return True

    @staticmethod
    @transaction.atomic
    def post_entry(entry):
        """
        Realiza el registro definitivo de un asiento contable (Paso 3).
        """
        if entry.is_posted:
             raise ValidationError("El asiento ya ha sido contabilizado.")

        AccountingEngine.validate_balance(entry)

        entry.is_posted = True
        entry.save()
        logger.info(f"Asiento {entry.id} contabilizado exitosamente via Engine.")
        return entry

    @staticmethod
    @transaction.atomic
    def post_subscription_entry(invoice):
        """
        Genera el impacto contable de una nueva suscripción SaaS.
        Impacta: 130505 (Clientes) vs 413501 (Ingresos SaaS)
        """
        # 1. Obtener/Crear periodo fiscal
        now = timezone.now()
        period, _ = FiscalPeriod.objects.get_or_create(
            name=now.strftime("%Y-%m"),
            defaults={
                'start_date': now.replace(day=1).date(),
                'end_date': (now + timezone.timedelta(days=32)).replace(day=1).date() - timezone.timedelta(days=1)
            }
        )

        # 2. Crear Asiento
        entry = JournalEntry.objects.create(
            date=now.date(),
            reference=invoice.number,
            description=f"Reconocimiento Ingreso SaaS - {invoice.number}",
            period=period
        )

        # 3. Obtener cuentas (según ChartOfAccountsManager/Directriz)
        acc_customers, _ = Account.objects.get_or_create(code="130505", defaults={'name': 'Clientes', 'account_type': 'ACTIVO'})
        acc_revenue, _ = Account.objects.get_or_create(code="413501", defaults={'name': 'Ingresos SaaS', 'account_type': 'INGRESOS'})

        # 4. Crear transacciones
        # Débito a Clientes
        Transaction.objects.create(
            entry=entry,
            account=acc_customers,
            debit=invoice.total_amount,
            credit=0
        )
        # Crédito a Ingresos
        Transaction.objects.create(
            entry=entry,
            account=acc_revenue,
            debit=0,
            credit=invoice.total_amount
        )

        # 5. Contabilizar
        return AccountingEngine.post_entry(entry)

from decimal import Decimal
from django.db.models import Sum
from .models import Account, LedgerEntry, JournalEntry

class ReportsEngine:
    """
    Engine for generating accounting and financial reports.
    Centralized for both Holding and Tenants.
    Implements CQRS Light: Read-only operations for reporting (Fase 6.3).
    """

    @staticmethod
    def get_read_db():
        """
        Determina qué base de datos usar para reportes.
        Si existe una réplica de lectura configurada, la usa.
        """
        from django.conf import settings
        if 'read_replica' in settings.DATABASES:
            return 'read_replica'
        return 'default'

    @staticmethod
    def get_p_and_l(tenant_id, start_date, end_date):
        """
        Generates Profit and Loss report (Income - Expenses).
        """
        # Cuentas de Ingresos (4) y Gastos (5)
        read_db = ReportsEngine.get_read_db()

        income_total = LedgerEntry.objects.using(read_db).filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__range=[start_date, end_date],
            journal_entry__is_posted=True,
            account__code__startswith='4'
        ).aggregate(balance=Sum('credit_amount') - Sum('debit_amount'))['balance'] or Decimal('0.00')

        expense_total = LedgerEntry.objects.using(read_db).filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__range=[start_date, end_date],
            journal_entry__is_posted=True,
            account__code__startswith='5'
        ).aggregate(balance=Sum('debit_amount') - Sum('credit_amount'))['balance'] or Decimal('0.00')

        return {
            "income": income_total,
            "expenses": expense_total,
            "net_profit": income_total - expense_total
        }

    @staticmethod
    def get_balance_sheet(tenant_id, cutoff_date):
        """
        Generates Balance Sheet (Assets, Liabilities, Equity).
        """
        read_db = ReportsEngine.get_read_db()

        asset_total = LedgerEntry.objects.using(read_db).filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='1'
        ).aggregate(balance=Sum('debit_amount') - Sum('credit_amount'))['balance'] or Decimal('0.00')

        liability_total = LedgerEntry.objects.using(read_db).filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='2'
        ).aggregate(balance=Sum('credit_amount') - Sum('debit_amount'))['balance'] or Decimal('0.00')

        equity_total = LedgerEntry.objects.using(read_db).filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='3'
        ).aggregate(balance=Sum('credit_amount') - Sum('debit_amount'))['balance'] or Decimal('0.00')

        return {
            "assets": asset_total,
            "liabilities": liability_total,
            "equity": equity_total,
            "check": asset_total - (liability_total + equity_total)
        }

    @staticmethod
    def get_trial_balance(tenant_id, cutoff_date):
        """
        Generates a detailed Trial Balance with all accounts.
        """
        read_db = ReportsEngine.get_read_db()

        accounts = Account.plain_objects.using(read_db).filter(tenant_id=tenant_id)
        lines = []
        for account in accounts:
            entries = LedgerEntry.objects.using(read_db).filter(
                journal_entry__tenant_id=tenant_id,
                journal_entry__date__lte=cutoff_date,
                journal_entry__is_posted=True,
                account=account
            ).aggregate(
                debit=Sum('debit_amount'),
                credit=Sum('credit_amount')
            )

            debit = entries['debit'] or Decimal('0.00')
            credit = entries['credit'] or Decimal('0.00')

            # Asset (1) and Expense (5) use Debit - Credit
            if account.code.startswith(('1', '5')):
                balance = debit - credit
            else:
                balance = credit - debit

            if debit != 0 or credit != 0:
                lines.append({
                    'account_code': account.code,
                    'account_name': account.name,
                    'debit': debit,
                    'credit': credit,
                    'balance': balance
                })

        return {
            'tenant_id': tenant_id,
            'cutoff_date': cutoff_date,
            'lines': lines
        }

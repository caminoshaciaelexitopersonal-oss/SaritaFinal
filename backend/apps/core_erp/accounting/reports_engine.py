from decimal import Decimal
from django.db.models import Sum
from .models import Account, LedgerEntry, JournalEntry

class ReportsEngine:
    """
    Engine for generating accounting and financial reports.
    Centralized for both Holding and Tenants.
    """

    @staticmethod
    def get_p_and_l(tenant_id, start_date, end_date):
        """
        Generates Profit and Loss report (Income - Expenses).
        """
        # Cuentas de Ingresos (4) y Gastos (5)
        income_total = LedgerEntry.objects.filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__range=[start_date, end_date],
            journal_entry__is_posted=True,
            account__code__startswith='4'
        ).aggregate(balance=Sum('credit_amount') - Sum('debit_amount'))['balance'] or Decimal('0.00')

        expense_total = LedgerEntry.objects.filter(
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
        asset_total = LedgerEntry.objects.filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='1'
        ).aggregate(balance=Sum('debit_amount') - Sum('credit_amount'))['balance'] or Decimal('0.00')

        liability_total = LedgerEntry.objects.filter(
            journal_entry__tenant_id=tenant_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='2'
        ).aggregate(balance=Sum('credit_amount') - Sum('debit_amount'))['balance'] or Decimal('0.00')

        equity_total = LedgerEntry.objects.filter(
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

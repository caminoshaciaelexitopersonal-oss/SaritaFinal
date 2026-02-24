from decimal import Decimal
from django.db.models import Sum
from .models import Account, JournalLine, JournalEntry

class ReportsEngine:
    """
    Engine for generating accounting and financial reports.
    Centralized for both Holding and Tenants.
    """

    @staticmethod
    def get_p_and_l(organization_id, start_date, end_date):
        """
        Generates Profit and Loss report (Income - Expenses).
        """
        # Cuentas de Ingresos (4) y Gastos (5)
        income_total = JournalLine.objects.filter(
            journal_entry__organization_id=organization_id,
            journal_entry__date__range=[start_date, end_date],
            journal_entry__is_posted=True,
            account__code__startswith='4'
        ).aggregate(balance=Sum('credit') - Sum('debit'))['balance'] or Decimal('0.00')

        expense_total = JournalLine.objects.filter(
            journal_entry__organization_id=organization_id,
            journal_entry__date__range=[start_date, end_date],
            journal_entry__is_posted=True,
            account__code__startswith='5'
        ).aggregate(balance=Sum('debit') - Sum('credit'))['balance'] or Decimal('0.00')

        return {
            "income": income_total,
            "expenses": expense_total,
            "net_profit": income_total - expense_total
        }

    @staticmethod
    def get_balance_sheet(organization_id, cutoff_date):
        """
        Generates Balance Sheet (Assets, Liabilities, Equity).
        """
        # Simplificado para F3
        asset_total = JournalLine.objects.filter(
            journal_entry__organization_id=organization_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='1'
        ).aggregate(balance=Sum('debit') - Sum('credit'))['balance'] or Decimal('0.00')

        liability_total = JournalLine.objects.filter(
            journal_entry__organization_id=organization_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='2'
        ).aggregate(balance=Sum('credit') - Sum('debit'))['balance'] or Decimal('0.00')

        equity_total = JournalLine.objects.filter(
            journal_entry__organization_id=organization_id,
            journal_entry__date__lte=cutoff_date,
            journal_entry__is_posted=True,
            account__code__startswith='3'
        ).aggregate(balance=Sum('credit') - Sum('debit'))['balance'] or Decimal('0.00')

        return {
            "assets": asset_total,
            "liabilities": liability_total,
            "equity": equity_total,
            "check": asset_total - (liability_total + equity_total)
        }

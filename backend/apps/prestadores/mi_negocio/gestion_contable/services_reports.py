# backend/apps/contabilidad/services_reports.py
from django.db.models import Sum
from django.db.models.functions import Coalesce
from .models import JournalEntry, ChartOfAccount, Transaction
def get_libro_diario(perfil, start_date, end_date):
    return JournalEntry.objects.filter(perfil=perfil, date__range=[start_date, end_date]).prefetch_related('transactions__account')
def get_libro_mayor(perfil, start_date, end_date):
    # Lógica simplificada para brevedad
    return ChartOfAccount.objects.filter(perfil=perfil, transaction__journal_entry__date__range=[start_date, end_date]).distinct()
def get_balance_sumas_saldos(perfil, end_date):
    return ChartOfAccount.objects.filter(perfil=perfil).annotate(total_debit=Sum('transaction__debit'), total_credit=Sum('transaction__credit'))
def get_estado_resultados(perfil, start_date, end_date):
    revenue = Transaction.objects.filter(account__perfil=perfil, account__account_type='REVENUE', journal_entry__date__range=[start_date, end_date]).aggregate(total=Coalesce(Sum('credit') - Sum('debit'), 0))['total']
    expenses = Transaction.objects.filter(account__perfil=perfil, account__account_type='EXPENSE', journal_entry__date__range=[start_date, end_date]).aggregate(total=Coalesce(Sum('debit') - Sum('credit'), 0))['total']
    return {'ingresos': revenue, 'gastos': expenses, 'utilidad_neta': revenue - expenses}
def get_balance_general(perfil, end_date):
    assets = ChartOfAccount.objects.filter(perfil=perfil, account_type='ASSET').aggregate(total=Sum('transaction__debit') - Sum('transaction__credit'))['total'] or 0
    liabilities = ChartOfAccount.objects.filter(perfil=perfil, account_type='LIABILITY').aggregate(total=Sum('transaction__credit') - Sum('transaction__debit'))['total'] or 0
    equity = ChartOfAccount.objects.filter(perfil=perfil, account_type='EQUITY').aggregate(total=Sum('transaction__credit') - Sum('transaction__debit'))['total'] or 0
    return {'activos': assets, 'pasivos': liabilities, 'patrimonio': equity}

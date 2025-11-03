from django.contrib import admin
from .models import (
    CostCenter,
    Currency,
    ExchangeRate,
    ChartOfAccount,
    JournalEntry,
    Transaction,
)

class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]
    list_display = ('id', 'entry_date', 'description', 'entry_type', 'user', 'created_at')
    search_fields = ('description', 'entry_type')
    list_filter = ('entry_date', 'entry_type')

@admin.register(ChartOfAccount)
class ChartOfAccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'nature', 'allows_transactions')
    search_fields = ('code', 'name')
    list_filter = ('nature', 'allows_transactions')

admin.site.register(CostCenter)
admin.site.register(Currency)
admin.site.register(ExchangeRate)

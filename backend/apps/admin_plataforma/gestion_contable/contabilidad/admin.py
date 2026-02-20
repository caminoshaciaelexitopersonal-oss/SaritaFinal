from django.contrib import admin
from .models import (
    AdminChartOfAccounts,
    AdminAccount,
    AdminFiscalPeriod,
    AdminJournalEntry,
    AdminAccountingTransaction,
)

class AdminAccountingTransactionInline(admin.TabularInline):
    model = AdminAccountingTransaction
    extra = 1

@admin.register(AdminJournalEntry)
class AdminJournalEntryAdmin(admin.ModelAdmin):
    inlines = [AdminAccountingTransactionInline]
    list_display = ('id', 'date', 'description', 'created_by')
    search_fields = ('description',)
    list_filter = ('date',)

@admin.register(AdminChartOfAccounts)
class AdminChartOfAccountsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(AdminAccount)
class AdminAccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'type')
    search_fields = ('code', 'name')
    list_filter = ('type',)

admin.site.register(AdminFiscalPeriod)

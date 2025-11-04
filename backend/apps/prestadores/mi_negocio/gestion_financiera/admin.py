from django.contrib import admin
from .models import BankAccount, CashTransaction

class CashTransactionInline(admin.TabularInline):
    model = CashTransaction
    extra = 0
    readonly_fields = ('created_by', 'created_at', 'journal_entry')
    can_delete = False

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'bank_name', 'account_number', 'perfil', 'is_active')
    search_fields = ('name', 'bank_name', 'account_number')
    list_filter = ('perfil', 'is_active')
    inlines = [CashTransactionInline]

@admin.register(CashTransaction)
class CashTransactionAdmin(admin.ModelAdmin):
    list_display = ('bank_account', 'transaction_date', 'transaction_type', 'amount', 'description')
    search_fields = ('bank_account__account_number', 'description')
    list_filter = ('transaction_type', 'transaction_date')
    date_hierarchy = 'transaction_date'
    readonly_fields = ('journal_entry',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

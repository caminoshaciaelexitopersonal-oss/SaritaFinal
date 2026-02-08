from django.contrib import admin
from .models import WalletAccount, WalletTransaction

@admin.register(WalletAccount)
class WalletAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'owner_type', 'balance', 'status', 'company')
    list_filter = ('owner_type', 'status', 'company')
    search_fields = ('user__username', 'owner_id')

@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'amount', 'status', 'timestamp')
    list_filter = ('type', 'status')
    search_fields = ('id', 'description')
    readonly_fields = ('timestamp',)

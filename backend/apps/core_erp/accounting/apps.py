from django.apps import AppConfig

class AccountingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core_erp.accounting'
    label = 'core_erp_accounting'
    verbose_name = 'Core ERP Accounting'

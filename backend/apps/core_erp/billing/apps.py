from django.apps import AppConfig

class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core_erp.billing'
    label = 'core_erp_billing'
    verbose_name = 'Core ERP Billing'

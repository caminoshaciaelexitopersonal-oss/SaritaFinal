from django.contrib import admin
from .models import (
    PlanDeCuentas,
    Cuenta,
    PeriodoContable,
    AsientoContable,
    Transaccion,
)

class TransaccionInline(admin.TabularInline):
    model = Transaccion
    extra = 1

@admin.register(AsientoContable)
class AsientoContableAdmin(admin.ModelAdmin):
    inlines = [TransaccionInline]
    list_display = ('id', 'date', 'description', 'creado_por')
    search_fields = ('description',)
    list_filter = ('date',)

@admin.register(PlanDeCuentas)
class PlanDeCuentasAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'account_type')
    search_fields = ('code', 'name')
    list_filter = ('account_type',)

admin.site.register(PeriodoContable)

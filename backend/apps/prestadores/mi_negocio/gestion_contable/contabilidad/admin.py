# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/admin.py
from django.contrib import admin
from .models import (
    PlanDeCuentas,
    Cuenta,
    PeriodoContable,
    AsientoContable,
    Transaccion,
)

class TransaccionInline(admin.TabularInline):
    """Permite editar transacciones directamente desde el asiento contable."""
    model = Transaccion
    extra = 2  # Muestra 2 líneas de transacción por defecto

@admin.register(AsientoContable)
class AsientoContableAdmin(admin.ModelAdmin):
    """Configuración del Admin para Asientos Contables."""
    inlines = [TransaccionInline]
    list_display = ('id', 'date', 'description', 'periodo', 'creado_por')
    search_fields = ('description',)
    list_filter = ('date', 'periodo')

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    """Configuración del Admin para Cuentas Contables."""
    list_display = ('code', 'name', 'type', 'plan_de_cuentas', 'parent')
    search_fields = ('code', 'name')
    list_filter = ('type', 'plan_de_cuentas')

@admin.register(PlanDeCuentas)
class PlanDeCuentasAdmin(admin.ModelAdmin):
    """Configuración del Admin para Planes de Cuentas."""
    list_display = ('name', 'provider', 'description')
    search_fields = ('name',)

@admin.register(PeriodoContable)
class PeriodoContableAdmin(admin.ModelAdmin):
    """Configuración del Admin para Períodos Contables."""
    list_display = ('id', 'period_start', 'period_end', 'status', 'provider')
    list_filter = ('status',)

# Nota: Transaccion se gestiona a través del inline en AsientoContableAdmin,
# pero también se puede registrar para acceso directo si se desea.
# admin.site.register(Transaccion)

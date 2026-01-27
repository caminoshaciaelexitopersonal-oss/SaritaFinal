# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/admin.py
from django.contrib import admin
from backend.models import (
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
    list_display = ('id', 'fecha', 'descripcion', 'periodo', 'creado_por')
    search_fields = ('descripcion',)
    list_filter = ('fecha', 'periodo')

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    """Configuración del Admin para Cuentas Contables."""
    list_display = ('codigo', 'nombre', 'tipo', 'plan_de_cuentas', 'parent')
    search_fields = ('codigo', 'nombre')
    list_filter = ('tipo', 'plan_de_cuentas')

@admin.register(PlanDeCuentas)
class PlanDeCuentasAdmin(admin.ModelAdmin):
    """Configuración del Admin para Planes de Cuentas."""
    list_display = ('nombre', 'provider', 'descripcion')
    search_fields = ('nombre',)

@admin.register(PeriodoContable)
class PeriodoContableAdmin(admin.ModelAdmin):
    """Configuración del Admin para Períodos Contables."""
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'cerrado', 'provider')
    list_filter = ('cerrado',)

# Nota: Transaccion se gestiona a través del inline en AsientoContableAdmin,
# pero también se puede registrar para acceso directo si se desea.
# admin.site.register(Transaccion)

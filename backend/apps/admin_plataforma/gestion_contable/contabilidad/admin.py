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
    list_display = ('id', 'fecha', 'descripcion', 'creado_por')
    search_fields = ('descripcion',)
    list_filter = ('fecha',)

@admin.register(PlanDeCuentas)
class PlanDeCuentasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo')
    search_fields = ('codigo', 'nombre')
    list_filter = ('tipo',)

admin.site.register(PeriodoContable)

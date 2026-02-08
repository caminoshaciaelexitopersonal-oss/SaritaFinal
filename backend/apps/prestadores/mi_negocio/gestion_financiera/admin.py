from django.contrib import admin
from .models import (
    CuentaBancaria, OrdenPago, TesoreriaCentral,
    EstadoResultados, BalanceGeneral, FlujoEfectivo,
    CambiosPatrimonio, ReservaFinanciera,
    ProyeccionFinanciera, RiesgoFinanciero
)

@admin.register(TesoreriaCentral)
class TesoreriaCentralAdmin(admin.ModelAdmin):
    list_display = ('provider', 'saldo_total_custodia', 'liquidez_disponible', 'reservas_totales')

@admin.register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'numero_cuenta', 'saldo_actual', 'activa')

@admin.register(OrdenPago)
class OrdenPagoAdmin(admin.ModelAdmin):
    list_display = ('concepto', 'monto', 'estado', 'fecha_pago')
    list_filter = ('estado', 'fecha_pago')

@admin.register(EstadoResultados)
class EstadoResultadosAdmin(admin.ModelAdmin):
    list_display = ('provider', 'periodo_contable_ref_id', 'utilidad_neta', 'fecha_generacion')

@admin.register(BalanceGeneral)
class BalanceGeneralAdmin(admin.ModelAdmin):
    list_display = ('provider', 'fecha_corte', 'total_activos', 'total_patrimonio')

@admin.register(ReservaFinanciera)
class ReservaFinancieraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'monto_objetivo', 'monto_actual')

@admin.register(ProyeccionFinanciera)
class ProyeccionFinancieraAdmin(admin.ModelAdmin):
    list_display = ('nombre_escenario', 'fecha_inicio', 'fecha_fin', 'nivel_probabilidad')

@admin.register(RiesgoFinanciero)
class RiesgoFinancieroAdmin(admin.ModelAdmin):
    list_display = ('tipo_riesgo', 'nivel', 'activo')
    list_filter = ('nivel', 'activo')

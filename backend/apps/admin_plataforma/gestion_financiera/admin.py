from django.contrib import admin
from .models import CuentaBancaria, TransaccionBancaria, OrdenPago

@admin.register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'numero_cuenta', 'saldo_actual')

@admin.register(TransaccionBancaria)
class TransaccionBancariaAdmin(admin.ModelAdmin):
    list_display = ('cuenta', 'monto', 'fecha')

@admin.register(OrdenPago)
class OrdenPagoAdmin(admin.ModelAdmin):
    list_display = ('concepto', 'monto', 'estado', 'fecha_pago')

from django.contrib import admin
from .models import CuentaBancaria, OrdenPago

@admin.register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'numero_cuenta', 'perfil', 'activa')

@admin.register(OrdenPago)
class OrdenPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_pago', 'monto', 'estado', 'perfil')

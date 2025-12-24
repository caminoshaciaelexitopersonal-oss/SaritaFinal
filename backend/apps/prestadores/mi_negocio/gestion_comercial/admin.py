from django.contrib import admin
from .domain.models import FacturaVenta, ItemFactura, ReciboCaja

class ItemFacturaInline(admin.TabularInline):
    model = ItemFactura
    extra = 1
    readonly_fields = ('subtotal',)

class ReciboCajaInline(admin.TabularInline):
    model = ReciboCaja
    extra = 0

@admin.register(FacturaVenta)
class FacturaVentaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'cliente', 'fecha_emision', 'total', 'total_pagado', 'estado', 'perfil')
    search_fields = ('numero_factura', 'cliente__nombre')
    list_filter = ('estado', 'fecha_emision', 'perfil')
    readonly_fields = ('subtotal', 'impuestos', 'total', 'total_pagado')
    inlines = [ItemFacturaInline, ReciboCajaInline]

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)
        form.instance.recalcular_totales()

@admin.register(ReciboCaja)
class ReciboCajaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'fecha_pago', 'monto', 'metodo_pago')
    search_fields = ('factura__numero_factura',)
    list_filter = ('metodo_pago', 'fecha_pago')
    date_hierarchy = 'fecha_pago'

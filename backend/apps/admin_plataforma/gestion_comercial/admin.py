from django.contrib import admin
from .domain.models import OperacionComercial, FacturaVenta, ItemFactura, ReciboCaja

class ItemOperacionInline(admin.TabularInline):
    model = ItemFactura # Wait, ItemOperacionComercial?
    extra = 1

@admin.register(OperacionComercial)
class OperacionComercialAdmin(admin.ModelAdmin):
    list_display = ('tipo_operacion', 'estado', 'total', 'fecha_creacion')
    list_filter = ('estado', 'tipo_operacion')

@admin.register(FacturaVenta)
class FacturaVentaAdmin(admin.ModelAdmin):
    list_display = ('number', 'issue_date')

@admin.register(ReciboCaja)
class ReciboCajaAdmin(admin.ModelAdmin):
    list_display = ('fecha_pago', 'monto')

admin.site.register(ItemFactura)

from django.contrib import admin
from .models import Proveedor, FacturaCompra

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit')

@admin.register(FacturaCompra)
class FacturaCompraAdmin(admin.ModelAdmin):
    list_display = ('numero', 'proveedor', 'fecha', 'total')

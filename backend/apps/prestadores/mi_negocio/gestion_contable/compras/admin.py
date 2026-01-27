from django.contrib import admin
from backend.models import Proveedor, FacturaCompra

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'identificacion', 'telefono', 'email', 'perfil')
    search_fields = ('nombre', 'identificacion')
    list_filter = ('perfil',)

@admin.register(FacturaCompra)
class FacturaCompraAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'proveedor', 'fecha_emision', 'total', 'estado', 'perfil')
    search_fields = ('numero_factura', 'proveedor__nombre')
    list_filter = ('estado', 'fecha_emision', 'perfil')
    date_hierarchy = 'fecha_emision'

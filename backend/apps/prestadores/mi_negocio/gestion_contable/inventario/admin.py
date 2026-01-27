from django.contrib import admin
from .models import Almacen, MovimientoInventario

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'perfil')
    search_fields = ('nombre',)
    list_filter = ('perfil',)

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo_movimiento', 'cantidad', 'almacen', 'fecha', 'usuario')
    search_fields = ('producto__nombre',)
    list_filter = ('tipo_movimiento', 'almacen', 'fecha')
    date_hierarchy = 'fecha'

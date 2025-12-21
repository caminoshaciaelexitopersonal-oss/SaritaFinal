from django.contrib import admin
from .models import CategoriaProducto, Producto, Almacen, MovimientoInventario

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'perfil')
    search_fields = ('nombre',)
    list_filter = ('perfil',)

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'perfil')
    search_fields = ('nombre',)
    list_filter = ('perfil',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sku', 'categoria', 'stock_actual', 'precio_venta', 'costo', 'perfil')
    search_fields = ('nombre', 'sku')
    list_filter = ('categoria', 'perfil')
    list_editable = ('stock_actual', 'precio_venta', 'costo')

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo_movimiento', 'cantidad', 'almacen', 'fecha', 'usuario')
    search_fields = ('producto__nombre',)
    list_filter = ('tipo_movimiento', 'almacen', 'fecha')
    date_hierarchy = 'fecha'

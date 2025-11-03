from django.contrib import admin
from .models import CategoriaActivo, ActivoFijo, Depreciacion

class DepreciacionInline(admin.TabularInline):
    model = Depreciacion
    extra = 1

@admin.register(CategoriaActivo)
class CategoriaActivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'perfil')
    search_fields = ('nombre',)
    list_filter = ('perfil',)

@admin.register(ActivoFijo)
class ActivoFijoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'fecha_adquisicion', 'valor_adquisicion', 'valor_en_libros', 'perfil')
    search_fields = ('nombre',)
    list_filter = ('categoria', 'fecha_adquisicion', 'perfil')
    inlines = [DepreciacionInline]

@admin.register(Depreciacion)
class DepreciacionAdmin(admin.ModelAdmin):
    list_display = ('activo', 'fecha', 'valor')
    search_fields = ('activo__nombre',)
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'

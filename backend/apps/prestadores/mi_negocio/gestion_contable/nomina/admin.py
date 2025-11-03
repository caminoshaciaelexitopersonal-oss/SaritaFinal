from django.contrib import admin
from .models import Empleado, Contrato, ConceptoNomina, Planilla, NovedadNomina

class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 0

class NovedadNominaInline(admin.TabularInline):
    model = NovedadNomina
    extra = 1

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'apellido', 'email', 'telefono', 'perfil')
    search_fields = ('nombre', 'apellido', 'identificacion')
    inlines = [ContratoInline]

@admin.register(ConceptoNomina)
class ConceptoNominaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'tipo')
    list_filter = ('tipo',)

@admin.register(Planilla)
class PlanillaAdmin(admin.ModelAdmin):
    list_display = ('periodo_inicio', 'periodo_fin', 'total_neto', 'perfil')
    date_hierarchy = 'periodo_inicio'
    inlines = [NovedadNominaInline]
    readonly_fields = ('total_devengado', 'total_deduccion', 'total_neto')

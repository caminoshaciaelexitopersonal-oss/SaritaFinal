from django.contrib import admin
from .models import Empleado, Contrato, ConceptoNomina, Planilla, NovedadNomina, DetalleLiquidacion

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha_inicio', 'salario_base')

@admin.register(Planilla)
class PlanillaAdmin(admin.ModelAdmin):
    list_display = ('anio', 'mes')

admin.site.register(ConceptoNomina)
admin.site.register(NovedadNomina)
admin.site.register(DetalleLiquidacion)

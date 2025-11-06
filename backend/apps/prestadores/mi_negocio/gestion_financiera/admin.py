from django.contrib import admin
from .models import CuentaBancaria, TransaccionBancaria

class TransaccionBancariaInline(admin.TabularInline):
    model = TransaccionBancaria
    extra = 0
    readonly_fields = ('creado_por', 'creado_en')
    can_delete = False

@admin.register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'numero_cuenta', 'tipo_cuenta', 'saldo_actual', 'titular', 'perfil')
    search_fields = ('banco', 'numero_cuenta', 'titular')
    list_filter = ('tipo_cuenta', 'perfil')
    inlines = [TransaccionBancariaInline]

@admin.register(TransaccionBancaria)
class TransaccionBancariaAdmin(admin.ModelAdmin):
    list_display = ('cuenta', 'fecha', 'tipo', 'monto', 'descripcion')
    search_fields = ('cuenta__numero_cuenta', 'descripcion')
    list_filter = ('tipo', 'fecha')
    date_hierarchy = 'fecha'

    def save_model(self, request, obj, form, change):
        if not obj.pk: # Si es un objeto nuevo
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)

from django.contrib import admin
from .models import (
Perfil,
ProductoServicio,
Cliente,
Inventario,
Costo,
CategoriaPrestador
)

@admin.register(CategoriaPrestador)
class CategoriaPrestadorAdmin(admin.ModelAdmin):
list_display = ('nombre', 'slug')
prepopulated_fields = {'slug': ('nombre',)}
admin.site.register(Perfil)
admin.site.register(ProductoServicio)
admin.site.register(Cliente)
admin.site.register(Inventario)
admin.site.register(Costo)

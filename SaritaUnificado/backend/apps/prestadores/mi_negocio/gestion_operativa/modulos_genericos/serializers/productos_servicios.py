from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios import ProductoServicio

class ProductoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicio
        fields = [
            'id', 'nombre', 'descripcion', 'precio', 'tipo',
            'cantidad_disponible', 'unidad_medida', 'activo'
        ]

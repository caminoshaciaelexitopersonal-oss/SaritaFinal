from rest_framework import serializers
from .models import Producto, Vacante, Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'notas', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion', 'prestador']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'activo', 'fecha_creacion', 'fecha_actualizacion']
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']

class VacanteSerializer(serializers.ModelSerializer):
    empresa_nombre = serializers.CharField(source='empresa.nombre_negocio', read_only=True)

    class Meta:
        model = Vacante
        fields = [
            'id', 'titulo', 'descripcion', 'tipo_contrato', 'ubicacion',
            'salario', 'fecha_publicacion', 'fecha_vencimiento', 'activa',
            'empresa', 'empresa_nombre'
        ]
        read_only_fields = ['id', 'fecha_publicacion', 'empresa', 'empresa_nombre']
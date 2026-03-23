from rest_framework import serializers
from django.apps import apps

OperacionComercial = apps.get_model('prestadores.mi_negocio.gestion_comercial.domain', 'OperacionComercial')
Cliente = apps.get_model('prestadores.mi_negocio.gestion_comercial.domain', 'Cliente')
Producto = apps.get_model('prestadores.mi_negocio.gestion_comercial.domain', 'Producto')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'tipo_cliente', 'limite_credito', 'perfil_ref_id']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'stock', 'categoria']

class OperacionSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = OperacionComercial
        fields = ['id', 'tipo_operacion', 'fecha', 'total', 'estado', 'cliente', 'productos', 'perfil_ref_id']
    
    def create(self, validated_data):
        validated_data['tenant'] = self.context['request'].tenant
        return super().create(validated_data)

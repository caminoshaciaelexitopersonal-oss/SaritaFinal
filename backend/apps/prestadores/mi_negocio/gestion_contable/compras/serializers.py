from rest_framework import serializers
from .models import Proveedor, FacturaCompra

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'identificacion', 'telefono', 'email', 'direccion']

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class FacturaCompraSerializer(serializers.ModelSerializer):
    proveedor_nombre = serializers.CharField(source='proveedor.nombre', read_only=True)
    creado_por = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FacturaCompra
        fields = [
            'id', 'proveedor', 'proveedor_nombre', 'numero_factura', 'fecha_emision',
            'fecha_vencimiento', 'subtotal', 'impuestos', 'total', 'estado',
            'notas', 'creado_por', 'creado_en'
        ]
        read_only_fields = ('creado_en',)
        extra_kwargs = {
            'proveedor': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_contable.inventario.models import CategoriaProducto, Almacen, Producto, MovimientoInventario

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['id', 'nombre', 'descripcion']

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = ['id', 'nombre', 'ubicacion']

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'sku', 'categoria', 'categoria_nombre', 'descripcion',
            'costo', 'precio_venta', 'stock_actual', 'stock_minimo'
        ]
        read_only_fields = ('stock_actual',) # El stock se maneja con movimientos

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

    def validate(self, data):
        costo = data.get('costo', 0)
        precio_venta = data.get('precio_venta', 0)
        stock_minimo = data.get('stock_minimo', 0)

        if costo < 0 or precio_venta < 0 or stock_minimo < 0:
            raise serializers.ValidationError("Los valores de costo, precio y stock no pueden ser negativos.")

        return data

class MovimientoInventarioSerializer(serializers.ModelSerializer):
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    almacen_nombre = serializers.CharField(source='almacen.nombre', read_only=True)

    class Meta:
        model = MovimientoInventario
        fields = [
            'id', 'producto', 'producto_nombre', 'almacen', 'almacen_nombre',
            'tipo_movimiento', 'cantidad', 'fecha', 'descripcion', 'usuario'
        ]
        read_only_fields = ('fecha',)

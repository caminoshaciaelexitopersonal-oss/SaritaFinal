from rest_framework import serializers
from .models import CategoriaMenu, ProductoMenu, Mesa, Pedido, ItemPedido

class ProductoMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoMenu
        fields = '__all__'

class CategoriaMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMenu
        fields = ['id', 'nombre']
        read_only_fields = ['prestador']

class CategoriaConProductosSerializer(serializers.ModelSerializer):
    productos = ProductoMenuSerializer(many=True, read_only=True)

    class Meta:
        model = CategoriaMenu
        fields = ['id', 'nombre', 'productos']

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
        read_only_fields = ['prestador']

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['producto', 'cantidad', 'precio_unitario']

class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'completado', 'total', 'items']
        read_only_fields = ['id', 'total']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        pedido = Pedido.objects.create(**validated_data)
        total = 0
        for item_data in items_data:
            producto = item_data['producto']
            cantidad = item_data['cantidad']
            precio = producto.precio
            total += precio * cantidad
            ItemPedido.objects.create(pedido=pedido, producto=producto, cantidad=cantidad, precio_unitario=precio)
        pedido.total = total
        pedido.save()
        return pedido
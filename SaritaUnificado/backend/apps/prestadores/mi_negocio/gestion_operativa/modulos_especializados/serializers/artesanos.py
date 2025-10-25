# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/serializers/artesanos.py
from rest_framework import serializers
from apps.prestadores.models import CategoriaProductoArtesanal, ProductoArtesanal, Pedido, DetallePedido

class CategoriaProductoArtesanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProductoArtesanal
        fields = ['id', 'nombre', 'descripcion']

class ProductoArtesanalSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = ProductoArtesanal
        fields = [
            'id', 'nombre', 'descripcion', 'precio', 'stock', 'foto',
            'materiales', 'tecnica', 'categoria', 'categoria_nombre', 'perfil'
        ]
        read_only_fields = ['id', 'categoria_nombre']

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetallePedido
        fields = ['id', 'producto', 'producto_nombre', 'cantidad', 'precio_unitario', 'subtotal']
        read_only_fields = ['id', 'subtotal', 'producto_nombre']

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = [
            'id', 'perfil', 'nombre_cliente', 'direccion_envio',
            'fecha_pedido', 'estado', 'total', 'detalles'
        ]
        read_only_fields = ['id', 'fecha_pedido', 'total']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        pedido = Pedido.objects.create(**validated_data)
        for detalle_data in detalles_data:
            DetallePedido.objects.create(pedido=pedido, **detalle_data)
        return pedido

    def update(self, instance, validated_data):
        # La actualización de detalles de un pedido puede ser compleja
        # y podría requerir lógica de negocio específica (ej. no cambiar si ya fue enviado).
        # Por ahora, solo actualizamos el estado.
        instance.estado = validated_data.get('estado', instance.estado)
        instance.save()
        return instance

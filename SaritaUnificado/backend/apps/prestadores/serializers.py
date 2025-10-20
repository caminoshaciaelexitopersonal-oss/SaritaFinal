from rest_framework import serializers
from .models import Perfil, CategoriaPrestador, Cliente, ProductoServicio, Inventario, Costo

class CategoriaPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPrestador
        fields = ['id', 'nombre', 'slug']

class PerfilSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Perfil
        fields = [
            'id', 'usuario_username', 'nombre_comercial', 'categoria', 'categoria_nombre',
            'telefono_principal', 'email_comercial', 'direccion', 'latitud', 'longitud',
            'descripcion_corta', 'logo', 'sitio_web', 'redes_sociales', 'estado',
            'puntuacion_total'
        ]
        read_only_fields = ['id', 'usuario_username', 'puntuacion_total']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ['perfil']

class ProductoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicio
        fields = '__all__'
        read_only_fields = ['perfil']

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'
        read_only_fields = ['perfil']

class CostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costo
        fields = '__all__'
        read_only_fields = ['perfil']

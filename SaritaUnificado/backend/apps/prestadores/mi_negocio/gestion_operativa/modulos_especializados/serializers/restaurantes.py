# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/serializers/restaurantes.py
from rest_framework import serializers
from apps.prestadores.models import CategoriaMenu, ProductoMenu, Mesa, ReservaMesa

class ProductoMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoMenu
        fields = ['id', 'nombre', 'descripcion', 'precio', 'foto', 'disponible', 'categoria']
        read_only_fields = ['id']

class CategoriaMenuSerializer(serializers.ModelSerializer):
    productos = ProductoMenuSerializer(many=True, read_only=True)

    class Meta:
        model = CategoriaMenu
        fields = ['id', 'nombre', 'descripcion', 'productos', 'perfil']
        read_only_fields = ['id']

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ['id', 'numero', 'capacidad', 'ubicacion', 'disponible', 'perfil']
        read_only_fields = ['id']

class ReservaMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaMesa
        fields = [
            'id', 'mesa', 'nombre_cliente', 'telefono_cliente',
            'fecha_hora', 'numero_personas', 'estado', 'notas'
        ]
        read_only_fields = ['id']

# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/perfil/serializers.py
from rest_framework import serializers
from .models import Perfil, CategoriaPrestador

class CategoriaPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPrestador
        fields = ['nombre', 'slug']

class PerfilSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo de Perfil del prestador.
    """
    categoria = serializers.StringRelatedField()
    usuario = serializers.StringRelatedField()

    class Meta:
        model = Perfil
        fields = [
            'id', 'usuario', 'nombre_comercial', 'categoria', 'telefono_principal',
            'email_comercial', 'direccion', 'latitud', 'longitud',
            'descripcion_corta', 'logo', 'sitio_web', 'redes_sociales',
            'estado', 'puntuacion_total'
        ]
        read_only_fields = ['usuario', 'estado', 'puntuacion_total']

class PerfilUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para actualizar el perfil del prestador.
    Permite la actualización de campos específicos.
    """
    class Meta:
        model = Perfil
        fields = [
            'nombre_comercial', 'telefono_principal', 'email_comercial',
            'direccion', 'latitud', 'longitud', 'descripcion_corta',
            'logo', 'sitio_web', 'redes_sociales'
        ]

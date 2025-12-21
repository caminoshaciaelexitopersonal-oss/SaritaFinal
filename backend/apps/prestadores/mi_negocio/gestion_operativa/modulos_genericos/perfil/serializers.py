# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/perfil/serializers.py
from rest_framework import serializers
from api.models import ProviderProfile, CategoriaPrestador

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
        model = ProviderProfile
        fields = [
            'id', 'usuario', 'nombre_comercial', 'provider_type', 'telefono_principal',
            'email_comercial', 'direccion', 'categoria',
            'is_verified'
        ]
        read_only_fields = ['usuario', 'is_verified']

class PerfilUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para actualizar el perfil del prestador.
    Permite la actualización de campos específicos.
    """
    class Meta:
        model = ProviderProfile
        fields = [
            'nombre_comercial', 'telefono_principal', 'email_comercial',
            'direccion',
            'logo', 'sitio_web', 'redes_sociales'
        ]

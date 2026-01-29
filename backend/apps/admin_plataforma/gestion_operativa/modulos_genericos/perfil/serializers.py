from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile, CategoriaPrestador

class CategoriaPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPrestador
        fields = ['nombre', 'slug']

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = [
            'id', 'usuario', 'nombre_comercial', 'provider_type', 'telefono_principal',
            'email_comercial', 'direccion', 'is_verified'
        ]
        read_only_fields = ['usuario', 'is_verified']

class PerfilUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = [
            'nombre_comercial', 'telefono_principal', 'email_comercial',
            'direccion'
        ]

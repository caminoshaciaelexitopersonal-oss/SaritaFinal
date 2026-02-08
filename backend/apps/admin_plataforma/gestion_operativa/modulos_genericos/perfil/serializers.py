from rest_framework import serializers
 
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile, CategoriaPrestador
 

class CategoriaPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPrestador
        fields = ['nombre', 'slug']

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = [
            'id', 'usuario', 'nombre_negocio', 'nit'
        ]
        read_only_fields = ['usuario']

class PerfilUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = [
            'nombre_negocio', 'nit'
        ]

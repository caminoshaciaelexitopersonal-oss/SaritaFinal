from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil import Perfil, CategoriaPrestador

class CategoriaPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPrestador
        fields = ['id', 'nombre', 'slug']

class PerfilSerializer(serializers.ModelSerializer):
    categoria = CategoriaPrestadorSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoriaPrestador.objects.all(), source='categoria', write_only=True
    )

    class Meta:
        model = Perfil
        fields = [
            'id', 'nombre_comercial', 'categoria', 'categoria_id', 'telefono_principal',
            'email_comercial', 'direccion', 'latitud', 'longitud',
            'descripcion_corta', 'logo', 'sitio_web', 'redes_sociales',
            'estado', 'puntuacion_total'
        ]
        read_only_fields = ['estado', 'puntuacion_total']

from rest_framework import serializers
from .models import CategoriaActivo, ActivoFijo, Depreciacion

class CategoriaActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaActivo
        fields = ['id', 'nombre']

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class ActivoFijoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = ActivoFijo
        fields = [
            'id', 'nombre', 'categoria', 'categoria_nombre', 'fecha_adquisicion',
            'valor_adquisicion', 'vida_util_meses', 'valor_residual', 'valor_en_libros'
        ]
        read_only_fields = ('valor_en_libros',)

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class DepreciacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depreciacion
        fields = ['id', 'activo', 'fecha', 'valor']

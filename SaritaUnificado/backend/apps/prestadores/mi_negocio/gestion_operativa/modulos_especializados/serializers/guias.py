# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/serializers/guias.py
from rest_framework import serializers
from apps.prestadores.models import Ruta, HitoRuta, Equipamiento

class HitoRutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitoRuta
        fields = ['id', 'nombre', 'descripcion', 'orden', 'latitud', 'longitud']
        read_only_fields = ['id']

class RutaSerializer(serializers.ModelSerializer):
    hitos = HitoRutaSerializer(many=True, read_only=True)

    class Meta:
        model = Ruta
        fields = [
            'id', 'nombre', 'descripcion_corta', 'descripcion_larga',
            'duracion_horas', 'distancia_km', 'dificultad', 'precio_persona',
            'punto_encuentro', 'foto_principal', 'hitos', 'perfil'
        ]
        read_only_fields = ['id']

class EquipamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamiento
        fields = [
            'id', 'nombre', 'descripcion', 'cantidad_total',
            'cantidad_disponible', 'foto', 'perfil'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        """
        Valida que la cantidad disponible no sea mayor a la total.
        """
        total = data.get('cantidad_total', self.instance.cantidad_total if self.instance else None)
        disponible = data.get('cantidad_disponible', self.instance.cantidad_disponible if self.instance else None)

        if total is not None and disponible is not None and disponible > total:
            raise serializers.ValidationError("La cantidad disponible no puede ser mayor que la cantidad total.")
        return data

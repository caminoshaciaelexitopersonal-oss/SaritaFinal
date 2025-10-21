from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.rat import RegistroActividadTuristica

class RegistroActividadTuristicaSerializer(serializers.ModelSerializer):
    archivo_url = serializers.FileField(source='archivo', read_only=True)

    class Meta:
        model = RegistroActividadTuristica
        fields = [
            'id', 'nombre_documento', 'descripcion', 'archivo', 'archivo_url',
            'fecha_presentacion', 'entidad_reguladora'
        ]
        extra_kwargs = {'archivo': {'write_only': True}}

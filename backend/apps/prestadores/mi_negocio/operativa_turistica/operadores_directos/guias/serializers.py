from rest_framework import serializers
from .models import (
    GuiaTuristico, CertificacionGuia, LocalRutaTuristica, Itinerario,
    GrupoTuristico, ServicioGuiado, LiquidacionGuia, IncidenciaServicio, Skill
)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificacionGuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificacionGuia
        fields = '__all__'

class GuiaTuristicoSerializer(serializers.ModelSerializer):
    certificaciones = CertificacionGuiaSerializer(many=True, read_only=True)
    full_name = serializers.ReadOnlyField(source='usuario.get_full_name')
    class Meta:
        model = GuiaTuristico
        fields = '__all__'

class ItinerarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerario
        fields = '__all__'

class LocalRutaTuristicaSerializer(serializers.ModelSerializer):
    itinerarios = ItinerarioSerializer(many=True, read_only=True)
    class Meta:
        model = LocalRutaTuristica
        fields = '__all__'

class GrupoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoTuristico
        fields = '__all__'

class ServicioGuiadoSerializer(serializers.ModelSerializer):
    ruta_nombre = serializers.ReadOnlyField(source='ruta.nombre')
    guia_nombre = serializers.ReadOnlyField(source='guia_asignado.usuario.get_full_name')
    class Meta:
        model = ServicioGuiado
        fields = '__all__'

class LiquidacionGuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiquidacionGuia
        fields = '__all__'

class IncidenciaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidenciaServicio
        fields = '__all__'

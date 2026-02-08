from rest_framework import serializers
from .models import MatrizRiesgo, ControlRiesgo, IncidenteLaboral, InvestigacionIncidente, SaludOcupacional, CapacitacionSST

class ControlRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlRiesgo
        fields = '__all__'

class MatrizRiesgoSerializer(serializers.ModelSerializer):
    controles = ControlRiesgoSerializer(many=True, read_only=True)
    class Meta:
        model = MatrizRiesgo
        fields = '__all__'

class InvestigacionIncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigacionIncidente
        fields = '__all__'

class IncidenteLaboralSerializer(serializers.ModelSerializer):
    investigacion = InvestigacionIncidenteSerializer(read_only=True)
    class Meta:
        model = IncidenteLaboral
        fields = '__all__'

class SaludOcupacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaludOcupacional
        fields = '__all__'

class CapacitacionSSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapacitacionSST
        fields = '__all__'

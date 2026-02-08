from rest_framework import serializers
from .models import ProcesoOperativo, TareaOperativa

class TareaOperativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaOperativa
        fields = '__all__'

class ProcesoOperativoSerializer(serializers.ModelSerializer):
    tareas = TareaOperativaSerializer(many=True, read_only=True)
    class Meta:
        model = ProcesoOperativo
        fields = '__all__'

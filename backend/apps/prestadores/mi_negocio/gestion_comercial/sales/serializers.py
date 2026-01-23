from rest_framework import serializers
from .models import Cliente, Opportunity

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'empresa', 'creado_en']
        read_only_fields = ('creado_en',)

    def create(self, validated_data):
        # Asigna automáticamente el perfil del prestador actual
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'name', 'stage', 'value', 'created_at']

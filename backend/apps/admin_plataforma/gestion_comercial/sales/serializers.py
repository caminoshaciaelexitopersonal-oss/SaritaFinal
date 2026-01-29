from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_comercial.sales.models import Opportunity

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'name', 'stage', 'value', 'created_at']

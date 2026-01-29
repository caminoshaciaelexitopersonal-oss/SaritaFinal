from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_genericos.clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ['provider']

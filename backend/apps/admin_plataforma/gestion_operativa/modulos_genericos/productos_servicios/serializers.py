from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['provider']

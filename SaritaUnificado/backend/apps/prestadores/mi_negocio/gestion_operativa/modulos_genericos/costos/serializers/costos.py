from rest_framework import serializers
from ...costos.models import Costo

class CostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costo
        fields = '__all__'

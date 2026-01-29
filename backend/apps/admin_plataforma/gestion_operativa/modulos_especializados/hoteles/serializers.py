from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_especializados.hoteles.models import Amenity, RoomType, Room

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'
        read_only_fields = ['provider']

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'
        read_only_fields = ['provider']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['provider']

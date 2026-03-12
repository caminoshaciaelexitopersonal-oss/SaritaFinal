from rest_framework import serializers
from .models import Room, RoomType, Amenity

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room_type_name = serializers.ReadOnlyField(source='room_type.product.nombre')

    class Meta:
        model = Room
        fields = '__all__'

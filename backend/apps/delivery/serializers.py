from rest_framework import serializers
from .models import DeliveryCompany, Driver, Vehicle, DeliveryService, DeliveryEvent

class DeliveryCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCompany
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Driver
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DeliveryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryEvent
        fields = '__all__'

class DeliveryServiceSerializer(serializers.ModelSerializer):
    events = DeliveryEventSerializer(many=True, read_only=True)
    class Meta:
        model = DeliveryService
        fields = '__all__'

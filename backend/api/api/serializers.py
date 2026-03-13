from rest_framework import serializers
from ..models import CustomUser, GovernmentProfile, TouristProfile, DeliveryProfile, Entity
from apps.turismo.models.provider_models import TourismProvider

class GovernmentProfileSerializer(serializers.ModelSerializer):
    entity_name = serializers.CharField(source='entity.name', read_only=True)
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = GovernmentProfile
        fields = '__all__'

class TouristProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = TouristProfile
        fields = '__all__'

class DeliveryProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = DeliveryProfile
        fields = '__all__'

class BusinessUserSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.get_full_name', read_only=True)

    class Meta:
        model = TourismProvider
        fields = '__all__'

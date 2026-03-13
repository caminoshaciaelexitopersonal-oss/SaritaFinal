from rest_framework import serializers
from ..models import CustomUser, GovernmentProfile, TouristProfile, DeliveryProfile, Entity, BusinessUserProfile
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

class BusinessProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    provider_name = serializers.CharField(source='provider.name', read_only=True)

    class Meta:
        model = BusinessUserProfile
        fields = '__all__'

class UserMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'first_name', 'last_name')

from rest_framework import serializers
from ..models import TourismDemandForecast, TourismSeasonality, TouristBehaviorProfile, TourismFlowAnalytics, TourismEconomicImpact

class TourismDemandForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismDemandForecast
        fields = '__all__'

class TourismSeasonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismSeasonality
        fields = '__all__'

class TouristBehaviorProfileSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='usuario.get_full_name', read_only=True)
    class Meta:
        model = TouristBehaviorProfile
        fields = '__all__'

class TourismFlowAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismFlowAnalytics
        fields = '__all__'

class TourismEconomicImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismEconomicImpact
        fields = '__all__'

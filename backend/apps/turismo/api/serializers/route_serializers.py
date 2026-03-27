from rest_framework import serializers
from ...models.routes import TourismRoute
from ...serializers.provider_serializers import TourismProviderSerializer
from api.serializers import AtractivoTuristicoListSerializer

class TourismRouteSerializer(serializers.ModelSerializer):
    attractions = AtractivoTuristicoListSerializer(many=True, read_only=True)
    providers = TourismProviderSerializer(many=True, read_only=True)

    class Meta:
        model = TourismRoute
        fields = '__all__'

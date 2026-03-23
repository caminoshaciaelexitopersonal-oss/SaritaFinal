from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import TourismDemandForecast, TourismSeasonality, TouristBehaviorProfile, TourismEconomicImpact
from .serializers import (
    TourismDemandForecastSerializer, TourismSeasonalitySerializer,
    TouristBehaviorProfileSerializer, TourismEconomicImpactSerializer
)
from ..services import TourismIntelligenceService, DynamicPricingService

class IntelligenceViewSet(viewsets.ViewSet):
    """
    Controlador central de Inteligencia Turística.
    """
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def forecast(self, request):
        destino = request.query_params.get('destino', 'Puerto Gaitán')
        categoria = request.query_params.get('categoria', 'ACCOMMODATION')
        fecha = request.query_params.get('fecha', '2026-04-01')

        forecast = TourismIntelligenceService.predict_demand(destino, categoria, fecha)
        serializer = TourismDemandForecastSerializer(forecast)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='economic-impact')
    def economic_impact(self, request):
        destino = request.query_params.get('destino', 'Puerto Gaitán')
        periodo = request.query_params.get('periodo', '2026-Q1')

        impact = TourismIntelligenceService.generate_economic_report(destino, periodo)
        serializer = TourismEconomicImpactSerializer(impact)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='suggest-price')
    def suggest_price(self, request):
        service_id = request.query_params.get('service_id')
        if not service_id:
            return Response({"error": "service_id required"}, status=status.HTTP_400_BAD_REQUEST)

        suggestion = DynamicPricingService.get_suggested_price(service_id)
        return Response(suggestion)

class TouristBehaviorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TouristBehaviorProfile.objects.all()
    serializer_class = TouristBehaviorProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class SeasonalityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TourismSeasonality.objects.all()
    serializer_class = TourismSeasonalitySerializer

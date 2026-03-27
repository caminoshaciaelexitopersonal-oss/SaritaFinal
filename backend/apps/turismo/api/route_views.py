from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.routes import TourismRoute
from .serializers.route_serializers import TourismRouteSerializer
from ..services.route_engine import IntelligentRouteEngine

class TourismRouteViewSet(viewsets.ModelViewSet):
    queryset = TourismRoute.objects.all()
    serializer_class = TourismRouteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['post'], url_path='generate-intelligent')
    def generate_intelligent(self, request):
        municipality_id = request.data.get('municipality_id')
        if not municipality_id:
            return Response({"error": "municipality_id required"}, status=400)

        routes = IntelligentRouteEngine.generate_routes_for_municipality(municipality_id)
        return Response(TourismRouteSerializer(routes, many=True).data)

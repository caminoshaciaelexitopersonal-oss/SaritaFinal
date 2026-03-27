from ..models.routes import TourismRoute
from ..models.provider_models import TourismProvider
from api.models import AtractivoTuristico
from django.db.models import Q

class IntelligentRouteEngine:
    """
    Motor inteligente para generar rutas turísticas territoriales basadas en
    la oferta (prestadores) y la demanda (atractivos/eventos).
    """

    @staticmethod
    def generate_routes_for_municipality(municipality_id):
        # 1. Analizar atractivos del municipio
        attractions = AtractivoTuristico.objects.filter(municipality_id=municipality_id)
        providers = TourismProvider.objects.filter(municipality_id=municipality_id, status='PUBLICADO')

        # Estrategia A: Ruta de Naturaleza (Agrupa atractivos de categoría BLANCO/Natural)
        nature_attractions = attractions.filter(categoria_color='BLANCO')
        if nature_attractions.count() >= 2:
            route, created = TourismRoute.objects.get_or_create(
                name=f"Ruta de la Naturaleza - {nature_attractions.first().municipality.name}",
                defaults={
                    "description": "Un recorrido por los tesoros naturales más impactantes del municipio.",
                    "department": nature_attractions.first().department,
                    "municipality": nature_attractions.first().municipality,
                    "route_type": "Naturaleza",
                    "is_intelligent": True
                }
            )
            route.attractions.set(nature_attractions)
            # Asociar prestadores de tipo GUÍA o AVENTURA
            route.providers.set(providers.filter(provider_type__in=['GUIDE', 'EXPERIENCE_PROVIDER']))

        # Estrategia B: Ruta Gastronómica
        restaurants = providers.filter(provider_type='RESTAURANT')
        if restaurants.count() >= 3:
            route, created = TourismRoute.objects.get_or_create(
                name=f"Ruta Gastronómica - {restaurants.first().municipality.name}",
                defaults={
                    "description": "Descubre los sabores auténticos del territorio.",
                    "department": restaurants.first().department,
                    "municipality": restaurants.first().municipality,
                    "route_type": "Gastronomía",
                    "is_intelligent": True
                }
            )
            route.providers.set(restaurants)

        return TourismRoute.objects.filter(municipality_id=municipality_id, is_intelligent=True)

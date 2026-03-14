import os
import django
import sys

# Setup Django
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.tourism_intelligence.models import TourismDemandForecast, TourismEconomicImpact, TourismSeasonality, TouristBehaviorProfile
from apps.tourism_intelligence.services import TourismIntelligenceService, DynamicPricingService
from apps.turismo.models.provider_models import TourismProvider, TourismService, Reservation
from api.models import CustomUser
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

def test_intelligence_flows():
    print("--- INICIANDO PRUEBAS DE INTELIGENCIA TURÍSTICA (VÍA 3) ---")

    try:
        # 1. Flow 14: Economic Impact and Indicator Generation
        owner, _ = CustomUser.objects.get_or_create(username="owner_intel", email="intel@test.com")
        provider = TourismProvider.objects.create(name="Intel Hotel", owner=owner, provider_type="HOTEL", location={"city": "Puerto Gaitán"})
        service = TourismService.objects.create(provider=provider, service_type="ACCOMMODATION", name="Habitación Pro", price=100000)
        tourist, _ = CustomUser.objects.get_or_create(username="turista_intel", email="tintel@test.com")

        # Create a completed reservation
        Reservation.objects.create(
            provider=provider,
            service=service,
            customer=tourist,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=1),
            total_price=100000,
            status="COMPLETED"
        )

        impact = TourismIntelligenceService.generate_economic_report("Puerto Gaitán", "2026-M3")
        print(f"✅ Flujo 14: Reporte económico generado. Ventas: {impact.ventas_totales}, Empleo: {impact.empleo_generado_estimado}.")

        # 2. Flow 15: Demand Prediction
        forecast = TourismIntelligenceService.predict_demand("Puerto Gaitán", "ACCOMMODATION", timezone.now().date())
        print(f"✅ Flujo 15: Predicción de demanda para hoy: {forecast.demanda_estimada} servicios.")

        # 3. Flow 16: Dynamic Pricing Logic
        TourismSeasonality.objects.create(destino="Puerto Gaitán", mes=timezone.now().month, nivel_demanda="HIGH")
        pricing = DynamicPricingService.get_suggested_price(service.id)
        print(f"✅ Flujo 16: Precio sugerido (Temporada Alta): {pricing['suggested_price']} (Base: {pricing['base_price']}). Razón: {pricing['adjustment_reason']}.")

        # 4. Flow 17: Behavior Profiling
        profile, _ = TouristBehaviorProfile.objects.get_or_create(
            usuario=tourist,
            defaults={
                "destinos_visitados": ["Puerto Gaitán"],
                "categorias_preferidas": ["HOTEL", "RESTAURANT"],
                "ticket_promedio": 150000,
                "segmento_asignado": "FAMILY"
            }
        )
        print(f"✅ Flujo 17: Perfil de comportamiento verificado para '{tourist.username}'. Segmento: {profile.get_segmento_asignado_display()}.")

        print("--- PRUEBAS DE INTELIGENCIA COMPLETADAS CON ÉXITO ---")

    except Exception as e:
        print(f"❌ ERROR EN LAS PRUEBAS DE INTELIGENCIA: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_intelligence_flows()

import os
import django
import uuid
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser, AtractivoTuristico
from apps.turismo.models.provider_models import TourismProvider
from apps.social.models import SocialMessage, SocialConversation
from apps.tourism_intelligence.models import ConversationalIntent, TourismEconomicImpact
from apps.tourism_intelligence.analytics_engine import ConversationalAnalyticsEngine
from rest_framework.test import APIClient

def verify_intelligence_flows():
    client = APIClient()
    admin = CustomUser.objects.get(username="admin_test")
    client.force_authenticate(user=admin)

    print("\n--- TEST 1: Conversational Intent Detection ---")
    # Create a conversation and message
    conv = SocialConversation.objects.create(id=uuid.uuid4())
    msg = SocialMessage.objects.create(
        id=uuid.uuid4(),
        conversation=conv,
        sender=admin,
        content="Hola, ¿dónde puedo encontrar un buen hotel en Puerto Gaitán? Es para reservar una habitación."
    )

    intent = ConversationalAnalyticsEngine.analyze_message(msg)
    print(f"Detected Intent: {intent.intent}")
    print(f"Confidence: {intent.confidence_score}")
    print(f"Sentiment: {intent.sentiment_score}")
    print(f"Entities: {intent.detected_entities}")

    print("\n--- TEST 2: Unified Dashboard Aggregation ---")
    # Setup some real data for aggregation
    TourismEconomicImpact.objects.update_or_create(
        destino="Puerto Gaitán", periodo="2026-Q1",
        defaults={"ventas_totales": Decimal("5000000.00"), "ingresos_turisticos_netos": Decimal("4500000.00")}
    )

    res = client.get("/api/v1/tourism/intelligence/intelligence/dashboard/")
    print(f"Dashboard via_3 total: {res.data['via_3']['total_interacciones']}")
    print(f"Dashboard via_2 average score: {res.data['via_2']['puntaje_promedio']}")
    print(f"Dashboard Economic Impact: {res.data['via_2']['impacto_economico']['ventas_totales'] if res.data['via_2']['impacto_economico'] else 'N/A'}")

    print("\n--- TEST 3: Territorial Filtering (DIVIPOLA) ---")
    from apps.turismo.models.divipola import Municipality
    mun = Municipality.objects.first()
    res = client.get(f"/api/v1/tourism/intelligence/intelligence/dashboard/?municipality={mun.id}")
    print(f"Territorial Dashboard Status: {res.data['status']}")
    print(f"Territorial Context: {res.data['territorial_context']}")

if __name__ == "__main__":
    try:
        verify_intelligence_flows()
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()

import os
import django
import sys

# Setup Django
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.turismo.models.provider_models import TourismProvider, BusinessProfile, TourismService
from apps.tourism_marketplace.models import TourismReview, ProviderReputation, ProductRanking
from django.db import transaction
from django.utils import timezone

def test_via_2_flows():
    print("--- INICIANDO PRUEBAS FUNCIONALES VÍA 2 (SECTOR PRIVADO) ---")

    try:
        # 1. Flow 11: Register provider with full metadata
        owner, _ = CustomUser.objects.get_or_create(username="prestador_full_v2", email="full2@test.com", defaults={"role": CustomUser.Role.BUSINESS_OWNER})
        provider = TourismProvider.objects.create(
            name="Agencia Aventuras del Meta 2",
            provider_type="TOUR_OPERATOR",
            owner=owner,
            location={"address": "Cra 5 # 12-30", "lat": 4.315, "lng": -72.085},
            contact={
                "phone": "3201112233",
                "whatsapp": "573201112233",
                "email": "aventuras2@meta.com",
                "facebook": "https://facebook.com/aventurasmeta2",
                "instagram": "https://instagram.com/aventurasmeta2"
            }
        )
        profile = BusinessProfile.objects.create(
            provider=provider,
            legal_name="Aventuras del Meta E.U. 2",
            tax_id="801.456.789-2",
            business_address="Cra 5 # 12-30",
            phone="3201112233",
            email="aventuras2@meta.com"
        )
        print(f"✅ Flujo 11: Prestador '{provider.name}' registrado con metadata completa y perfil legal.")

        # 2. Flow 12: Publish Product and Experience
        tour_product = TourismService.objects.create(
            provider=provider,
            service_type="TOUR",
            name="Ruta del Delfín Rosado 2",
            description="Recorrido fluvial por el Manacacías",
            price=120000,
            capacity=10
        )
        culture_exp = TourismService.objects.create(
            provider=provider,
            service_type="EXPERIENCE",
            name="Tarde Llanera: Cantos y Vaquería 2",
            description="Inmersión en la cultura del hato",
            price=85000,
            capacity=15
        )
        print(f"✅ Flujo 12: Producto '{tour_product.name}' y Experiencia '{culture_exp.name}' publicados.")

        # 3. Flow 13: Reputation Logic Simulation
        tourist, _ = CustomUser.objects.get_or_create(username="critico_turismo", email="critico@test.com", defaults={"role": CustomUser.Role.TURISTA})
        review = TourismReview.objects.create(
            customer=tourist,
            service=tour_product,
            rating=5,
            comment="Increíble experiencia, recomendada!",
            is_verified_purchase=True
        )

        # Update Analytics/Reputation
        reputation, _ = ProviderReputation.objects.get_or_create(provider=provider)
        reputation.total_reviews += 1
        reputation.rating_promedio = 5.0
        reputation.save()

        ranking, _ = ProductRanking.objects.get_or_create(service=tour_product)
        ranking.indice_reputacion = 1.0
        ranking.calculate_total_score()

        print(f"✅ Flujo 13: Reseña de '{tourist.username}' procesada. Reputación de '{provider.name}' actualizada (Score: {ranking.score_total}).")

        print("--- PRUEBAS VÍA 2 COMPLETADAS CON ÉXITO ---")

    except Exception as e:
        print(f"❌ ERROR EN LAS PRUEBAS VÍA 2: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_via_2_flows()

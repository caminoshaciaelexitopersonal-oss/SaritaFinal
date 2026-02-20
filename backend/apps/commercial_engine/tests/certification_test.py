import os
import django
import uuid
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.commercial_engine.lead_model import Lead
from apps.commercial_engine.plan_model import Plan
from apps.commercial_engine.lead_scoring_engine import LeadScoringEngine
from apps.commercial_engine.conversion_orchestrator import ConversionOrchestrator
from apps.commercial_engine.kpi_engine import KpiEngine

def run_certification_test():
    print("--- INICIANDO CERTIFICACIÓN FASE 2 ---")

    # 1. Crear un plan de prueba
    plan, _ = Plan.objects.get_or_create(
        name="Plan Professional",
        defaults={
            'monthly_price': Decimal('99.00'),
            'annual_price': Decimal('990.00'),
            'billing_type': Plan.BillingType.FLAT
        }
    )

    success_count = 0
    for i in range(10):
        try:
            # 2. Crear Lead
            lead = Lead.objects.create(
                company_name=f"Empresa Cert {i}_{uuid.uuid4().hex[:4]}",
                contact_email=f"cert_{i}@example.com",
                estimated_size='ENTERPRISE',
                industry='TURISMO',
                utm_source='ads'
            )

            # 3. Calificar automáticamente
            score = LeadScoringEngine.update_score(lead)
            lead.refresh_from_db()

            if lead.status != Lead.Status.QUALIFIED:
                print(f"ERROR: Lead {i} no calificado. Score: {score}")
                continue

            # 4. Convertir autónomamente
            result = ConversionOrchestrator.convert_lead_to_subscription(lead.id, plan.id)

            if result['status'] == 'SUCCESS':
                success_count += 1
                print(f"EXITO: Lead {i} convertido. Company ID: {result['company_id']}")

        except Exception as e:
            print(f"FALLO en iteración {i}: {e}")

    print(f"\n--- RESULTADO FINAL: {success_count}/10 conversiones exitosas ---")

    # Verificar KPIs
    kpis = KpiEngine.get_all_kpis()
    print(f"KPIs Finales: {kpis}")

    if success_count == 10:
        print("✅ FASE 2 CERTIFICADA EXITOSAMENTE.")
    else:
        print("❌ FASE 2 NO SUPERADA.")

if __name__ == "__main__":
    run_certification_test()

import logging
from .models import SaaSLead, SaaSPlan, SaaSSubscription
from .lead_scoring import LeadScoringEngine
from .subscription_engine import SubscriptionEngine
from apps.core_erp.billing_engine import BillingEngine
from apps.core_erp.accounting_engine import AccountingEngine
from django.db import transaction

logger = logging.getLogger(__name__)

class PipelineEngine:
    """
    Orquestador del ciclo comercial SaaS (Fase 3/Bloque 2).
    """

    @staticmethod
    @transaction.atomic
    def process_conversion(lead_id, plan_id):
        lead = SaaSLead.objects.get(id=lead_id)
        plan = SaaSPlan.objects.get(id=plan_id)

        # 1. Calificar
        LeadScoringEngine.score_lead(lead)
        if not LeadScoringEngine.should_qualify(lead):
            logger.warning(f"Lead {lead.company_name} no cumple con el puntaje mínimo.")
            return None

        # 2. Crear Suscripción
        subscription = SubscriptionEngine.create_subscription(lead, plan)

        # 3. Marcar lead como convertido
        lead.status = SaaSLead.Status.CONVERTED
        lead.save()

        logger.info(f"Ciclo comercial completado para {lead.company_name}.")
        return subscription

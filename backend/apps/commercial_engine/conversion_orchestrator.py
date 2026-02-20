import logging
from django.db import transaction
from django.utils import timezone
from apps.companies.models import Company
from .lead_model import Lead
from .plan_model import Plan
from .subscription_engine import Subscription, SubscriptionEngine
from .pipeline_engine import PipelineEngine
from .events import EventBus
from apps.core_erp.billing.billing_engine import BillingEngine
from apps.core_erp.accounting.accounting_engine import AccountingEngine

logger = logging.getLogger(__name__)

class ConversionOrchestrator:
    """
    Cerebro de conversión: Orquesta el flujo desde Lead calificado hasta Suscripción activa.
    """

    @staticmethod
    @transaction.atomic
    def convert_lead_to_subscription(lead_id, plan_id, user=None):
        """
        Ejecuta el flujo completo de conversión con rollback total en caso de error.
        """
        try:
            # 1. Validar lead y plan
            lead = Lead.objects.get(id=lead_id)
            plan = Plan.objects.get(id=plan_id)

            if lead.status != Lead.Status.QUALIFIED and lead.status != Lead.Status.NEW:
                raise ValueError(f"El Lead {lead_id} no está calificado para conversión.")

            logger.info(f"Iniciando conversión para {lead.company_name}")

            # 2. Crear empresa (Tenant) en core_erp / apps.companies
            company_code = lead.company_name[:3].upper() + timezone.now().strftime("%H%M")
            company = Company.objects.create(
                name=lead.company_name,
                code=company_code,
                is_active=False # Aún no activado
            )

            # 3. Crear suscripción
            subscription = Subscription.objects.create(
                company_id=company.id,
                plan=plan,
                status=Subscription.Status.TRIAL,
                mrr=plan.monthly_price,
                billing_cycle='monthly'
            )

            # 4. Generar factura inicial (vía BillingEngine)
            # Nota: El BillingEngine debe ser capaz de crear la factura.
            # Pasamos datos necesarios para que el Engine orqueste.
            invoice_data = {
                'client_name': lead.company_name,
                'amount': plan.monthly_price,
                'concept': f"Suscripción SaaS - Plan {plan.name}"
            }
            invoice = BillingEngine.create_invoice(company, invoice_data)

            # 5. Registrar asiento contable (vía AccountingEngine)
            # El engine debe generar el impacto en 130505 vs 413501
            entry = AccountingEngine.post_subscription_entry(invoice)

            # 6. Activar tenant / suscripción
            subscription = SubscriptionEngine.activate_subscription(subscription, user=user)
            company.is_active = True
            company.save()

            # 7. Actualizar pipeline
            PipelineEngine.transition_to(lead, 'CONVERTED', user=user, reason="Conversion successful")

            # 8. Notificar éxito
            EventBus.publish('LEAD_CONVERTED', {
                'lead_id': str(lead.id),
                'company_id': str(company.id),
                'subscription_id': str(subscription.id),
                'invoice_id': str(invoice.id)
            }, user=user)

            logger.info(f"Conversión EXITOSA: {lead.company_name} es ahora un cliente activo.")

            return {
                'status': 'SUCCESS',
                'company_id': company.id,
                'subscription_id': subscription.id
            }

        except Exception as e:
            logger.error(f"FALLO en conversión de Lead {lead_id}: {str(e)}")
            # El decorador @transaction.atomic se encarga del rollback
            raise e

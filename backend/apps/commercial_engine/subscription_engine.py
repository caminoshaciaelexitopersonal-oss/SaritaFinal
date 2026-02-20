import uuid
import logging
from django.db import models
from django.utils import timezone
from .plan_model import Plan
from .events import EventBus

logger = logging.getLogger(__name__)

class Subscription(models.Model):
    class Status(models.TextChoices):
        TRIAL = 'trial', 'Trial'
        ACTIVE = 'active', 'Active'
        SUSPENDED = 'suspended', 'Suspended'
        CANCELLED = 'cancelled', 'Cancelled'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.UUIDField() # ID de la empresa en core_erp
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TRIAL
    )
    start_date = models.DateTimeField(default=timezone.now)
    renewal_date = models.DateTimeField(null=True, blank=True)
    billing_cycle = models.CharField(max_length=20, default='monthly')
    mrr = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return f"Sub {self.id} - Company {self.company_id}"

    class Meta:
        app_label = 'commercial_engine'

class SubscriptionEngine:
    """
    Motor encargado de la lógica de activación y gestión de suscripciones.
    """

    @staticmethod
    def activate_subscription(subscription: Subscription, user=None):
        """
        Activa una suscripción, genera factura inicial e impacta ERP.
        """
        subscription.status = Subscription.Status.ACTIVE
        subscription.save()

        # Disparar evento
        EventBus.publish('SUBSCRIPTION_ACTIVATED', {
            'subscription_id': str(subscription.id),
            'company_id': str(subscription.company_id),
            'mrr': float(subscription.mrr)
        }, user=user)

        logger.info(f"Suscripción {subscription.id} ACTIVADA para empresa {subscription.company_id}")
        return subscription

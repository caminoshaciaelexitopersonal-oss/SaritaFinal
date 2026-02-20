import uuid
import logging
from django.db import models
from django.db.models import Sum
from .events import EventBus

logger = logging.getLogger(__name__)

class KpiMetric(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'commercial_engine'

class KpiEngine:
    """
    Motor de KPIs en tiempo real.
    """

    @staticmethod
    def initialize():
        """
        Suscribe el engine a los eventos relevantes.
        """
        EventBus.subscribe('SUBSCRIPTION_ACTIVATED', KpiEngine.handle_subscription_activated)
        EventBus.subscribe('SUBSCRIPTION_CANCELLED', KpiEngine.handle_subscription_cancelled)
        logger.info("KpiEngine inicializado y suscrito a eventos.")

    @staticmethod
    def handle_subscription_activated(payload):
        """
        Actualiza MRR cuando una suscripción se activa.
        """
        mrr_delta = payload.get('mrr', 0)
        metric, _ = KpiMetric.objects.get_or_create(name='MRR')
        metric.value = float(metric.value) + float(mrr_delta)
        metric.save()

        # También actualizar ARR
        arr_metric, _ = KpiMetric.objects.get_or_create(name='ARR')
        arr_metric.value = float(metric.value) * 12
        arr_metric.save()

        logger.info(f"KPI Updated: MRR={metric.value}, ARR={arr_metric.value}")

    @staticmethod
    def handle_subscription_cancelled(payload):
        """
        Resta del MRR cuando una suscripción se cancela.
        """
        mrr_delta = payload.get('mrr', 0)
        metric, _ = KpiMetric.objects.get_or_create(name='MRR')
        metric.value = max(0, float(metric.value) - float(mrr_delta))
        metric.save()

        arr_metric, _ = KpiMetric.objects.get_or_create(name='ARR')
        arr_metric.value = float(metric.value) * 12
        arr_metric.save()

        logger.info(f"KPI Updated (Churn): MRR={metric.value}")

    @staticmethod
    def get_all_kpis():
        return {m.name: m.value for m in KpiMetric.objects.all()}

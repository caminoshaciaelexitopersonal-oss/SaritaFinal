from celery import shared_task
import logging
from .metrics import TechnicalMonitor

logger = logging.getLogger(__name__)

@shared_task(name="broadcast_system_metrics_task")
def broadcast_system_metrics_task():
    """
    Tarea periódica para emitir el pulso técnico del sistema.
    """
    try:
        TechnicalMonitor.broadcast_metrics()
    except Exception as e:
        logger.error(f"Error en tarea de métricas: {e}")

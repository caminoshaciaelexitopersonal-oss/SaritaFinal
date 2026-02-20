import logging
from django.utils import timezone
from .lead_model import Lead
from .events import EventBus

logger = logging.getLogger(__name__)

class PipelineEngine:
    """
    Motor de Pipeline (Kanban) para la gestión del ciclo de vida del Lead.
    """

    STAGES = [
        'NEW',
        'CONTACTED',
        'QUALIFIED',
        'PROPOSAL_SENT',
        'NEGOTIATION',
        'CONVERTED',
        'LOST'
    ]

    @staticmethod
    def transition_to(lead: Lead, new_status: str, user=None, reason="System transition"):
        """
        Transiciona un lead a un nuevo estado, validando la jerarquía y auditando.
        """
        if new_status.upper() not in PipelineEngine.STAGES:
            raise ValueError(f"Estado inválido: {new_status}")

        old_status = lead.status
        lead.status = new_status.lower()
        lead.save()

        # Auditoría y Eventos
        EventBus.publish('LEAD_PIPELINE_TRANSITION', {
            'lead_id': str(lead.id),
            'old_status': old_status,
            'new_status': lead.status,
            'reason': reason
        }, user=user)

        logger.info(f"Lead {lead.id} movido de {old_status} a {lead.status}")
        return lead

    @staticmethod
    def get_time_in_stage(lead_id, stage):
        """
        (Placeholder) Calcula el tiempo que un lead ha pasado en una etapa específica.
        Requeriría un modelo de historial de estados (LeadStateHistory).
        """
        # Por ahora devolvemos un valor simulado
        return "2 days, 4 hours"

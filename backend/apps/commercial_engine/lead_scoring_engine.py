import logging
from .lead_model import Lead
from .events import EventBus

logger = logging.getLogger(__name__)

class LeadScoringEngine:
    """
    Motor encargado de calificar la calidad de los prospectos (leads)
    basado en criterios de negocio predefinidos.
    """

    THRESHOLD = 70.0

    @staticmethod
    def calculate_score(lead: Lead) -> float:
        """
        Asigna puntaje automático basado en:
        - Tamaño empresa (estimated_size)
        - Industria (industry)
        - Origen UTM (utm_source)
        """
        score = 0.0

        # 1. Tamaño empresa
        size_weights = {
            'ENTERPRISE': 40,
            'MEDIUM': 25,
            'SMALL': 10,
            'STARTUP': 15
        }
        if lead.estimated_size:
            score += size_weights.get(lead.estimated_size.upper(), 0)

        # 2. Industria
        priority_industries = ['TURISMO', 'HOTELERIA', 'VIAJES', 'TECNOLOGIA']
        if lead.industry and lead.industry.upper() in priority_industries:
            score += 20

        # 3. Origen UTM
        if lead.utm_source and lead.utm_source.lower() in ['ads', 'referral', 'campaign']:
            score += 20
        elif lead.source and lead.source.lower() == 'organic':
            score += 10

        return float(min(score, 100))

    @staticmethod
    def update_score(lead: Lead):
        """
        Actualiza el puntaje del lead y dispara evento si califica.
        """
        old_status = lead.status
        lead.score = LeadScoringEngine.calculate_score(lead)

        if lead.score >= LeadScoringEngine.THRESHOLD and lead.status == Lead.Status.NEW:
            lead.status = Lead.Status.QUALIFIED
            lead.save()

            # Disparar evento LEAD_QUALIFIED
            EventBus.publish('LEAD_QUALIFIED', {
                'lead_id': str(lead.id),
                'score': lead.score,
                'company_name': lead.company_name
            })
            logger.info(f"Lead {lead.id} calificado con score {lead.score}")
        else:
            lead.save()

        return lead.score

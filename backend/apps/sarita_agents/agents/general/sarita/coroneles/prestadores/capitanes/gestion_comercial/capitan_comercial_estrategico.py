# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_comercial/capitan_comercial_estrategico.py
import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import Mision, PlanTáctico

logger = logging.getLogger(__name__)

class CapitanComercialEstrategico(CapitanTemplate):
    """
    Agente Comercial Estratégico: Analiza el rendimiento comercial y sugiere optimizaciones.
    """

    def plan(self, mision: Mision) -> PlanTáctico:
        logger.info(f"CAPITÁN (Estratégico): Analizando estrategia comercial para misión {mision.id}")

        pasos = {
            "analisis_roi_cac": {
                "descripcion": "Calcular indicadores de eficiencia comercial (CAC, ROI).",
                "teniente": "roi_calculator", # Ya existe en TENIENTE_MAP
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }

        return PlanTáctico.objects.create(
            mision=mision,
            capitan_responsable=self.__class__.__name__,
            pasos_del_plan=pasos,
            estado='PLANIFICADO'
        )

    def _get_tenientes(self) -> dict:
        # roi_calculator se importa de tasks.py indirectamente a través del orquestador,
        # pero aquí necesitamos registrarlo en el roster local del capitán para S-0.4
        from apps.sarita_agents.tasks import TenienteROICalculator
        return {
            "roi_calculator": TenienteROICalculator()
        }

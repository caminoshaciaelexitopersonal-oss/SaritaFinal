import abc
import logging
from typing import Dict, Any
from ..models import StrategyProposal

logger = logging.getLogger(__name__)

class CapitanDecisorBase(abc.ABC):
    """
    Base para todos los Agentes Decisores de SARITA.
    Analizan datos y proponen acciones estratégicas.
    """
    domain = None

    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    @abc.abstractmethod
    def analyze_and_propose(self, data: Dict[str, Any]) -> StrategyProposal:
        """
        Analiza un set de datos y genera una Propuesta Estratégica.
        """
        pass

    def _create_proposal(self, **kwargs) -> StrategyProposal:
        """Helper para persistir la propuesta."""
        return StrategyProposal.objects.create(
            domain=self.domain,
            agent_id=self.agent_id,
            **kwargs
        )

class CapitanDecisorFinanciero(CapitanDecisorBase):
    domain = StrategyProposal.Domain.FINANCIERO

    def analyze_and_propose(self, data: Dict[str, Any]) -> StrategyProposal:
        logger.info(f"AGENTE FINANCIERO ({self.agent_id}): Analizando salud económica...")
        # Lógica de análisis simulada para la fase inicial
        # En el futuro, esto consultará el ERP Sistémico
        return self._create_proposal(
            contexto_detectado="Incremento en la tasa de cancelación de suscripciones detectado en los últimos 30 días (15%).",
            riesgo_actual="Pérdida proyectada de $5,000 USD en ingresos recurrentes trimestrales.",
            oportunidad_detectada="Fidelización de usuarios en riesgo mediante ajustes en planes semestrales.",
            accion_sugerida={
                "intention": "PLATFORM_UPDATE_PLAN",
                "parameters": {"descuento_retencion": 0.20, "target_segment": "at_risk"}
            },
            impacto_estimado="Reducción del churn en un 5% y recuperación de $2,000 USD.",
            nivel_confianza=0.85,
            nivel_urgencia=StrategyProposal.UrgencyLevel.HIGH,
            nivel_riesgo=StrategyProposal.RiskLevel.MEDIUM
        )

class CapitanDecisorOperativo(CapitanDecisorBase):
    domain = StrategyProposal.Domain.OPERATIVO

    def analyze_and_propose(self, data: Dict[str, Any]) -> StrategyProposal:
        logger.info(f"AGENTE OPERATIVO ({self.agent_id}): Analizando desempeño...")
        return self._create_proposal(
            contexto_detectado="Saturación de procesamiento de documentos en el módulo de archivística (90% capacidad).",
            riesgo_actual="Retraso en la verificación de nuevos prestadores (Onboarding).",
            oportunidad_detectada="Optimización de carga asíncrona y escalado de workers Celery.",
            accion_sugerida={
                "intention": "PLATFORM_OPTIMIZE_RESOURCES",
                "parameters": {"worker_boost": 2, "priority": "high"}
            },
            impacto_estimado="Reducción de tiempo de espera de 48h a 12h.",
            nivel_confianza=0.92,
            nivel_urgencia=StrategyProposal.UrgencyLevel.MEDIUM,
            nivel_riesgo=StrategyProposal.RiskLevel.LOW
        )

class CapitanDecisorComercial(CapitanDecisorBase):
    domain = StrategyProposal.Domain.COMERCIAL

    def analyze_and_propose(self, data: Dict[str, Any]) -> StrategyProposal:
        logger.info(f"AGENTE COMERCIAL ({self.agent_id}): Analizando funnel de ventas...")
        return self._create_proposal(
            contexto_detectado="Alta tasa de rebote en la página de checkout detectada.",
            riesgo_actual="Pérdida de conversiones potenciales del 40% durante la última semana.",
            oportunidad_detectada="Simplificación del formulario de pago y habilitación de nuevos métodos.",
            accion_sugerida={
                "intention": "PLATFORM_UPDATE_WEB_CMS",
                "parameters": {"layout": "simplified_checkout", "enable_express_pay": True}
            },
            impacto_estimado="Incremento proyectado del 10% en conversiones.",
            nivel_confianza=0.78,
            nivel_urgencia=StrategyProposal.UrgencyLevel.HIGH,
            nivel_riesgo=StrategyProposal.RiskLevel.LOW
        )

class CapitanDecisorNormativo(CapitanDecisorBase):
    domain = StrategyProposal.Domain.NORMATIVO

    def analyze_and_propose(self, data: Dict[str, Any]) -> StrategyProposal:
        logger.info(f"AGENTE NORMATIVO ({self.agent_id}): Verificando cumplimiento...")
        return self._create_proposal(
            contexto_detectado="Nueva regulación de protección de datos (Ley 1581) requiere actualización de términos.",
            riesgo_actual="Sanciones legales potenciales por incumplimiento de política de privacidad.",
            oportunidad_detectada="Actualización proactiva para generar confianza en los prestadores.",
            accion_sugerida={
                "intention": "PLATFORM_UPDATE_LEGAL",
                "parameters": {"version": "2.1", "enforce_acceptance": True}
            },
            impacto_estimado="Cumplimiento del 100% del marco legal vigente.",
            nivel_confianza=1.0,
            nivel_urgencia=StrategyProposal.UrgencyLevel.CRITICAL,
            nivel_riesgo=StrategyProposal.RiskLevel.HIGH
        )

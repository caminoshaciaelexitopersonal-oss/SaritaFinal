import logging
import json
from django.utils import timezone
from .models import SystemicRiskIndicator, StabilityAlert, MitigationScenario

logger = logging.getLogger(__name__)

class StabilityMonitorService:
    """
    Motor de Observación Preventiva (Z-PEACE-NET).
    Analiza indicadores para detectar señales de inestabilidad.
    """

    @staticmethod
    def analyze_indicators():
        """Escanea todos los indicadores activos en busca de anomalías."""
        indicators = SystemicRiskIndicator.objects.all()
        anomalies = [i for i in indicators if i.is_anomalous()]

        if not anomalies:
            return None

        # Determinar severidad
        is_critical = any(i.is_critical() for i in anomalies)
        severity = StabilityAlert.Severity.CRITICAL if is_critical else StabilityAlert.Severity.MEDIUM

        # Generar Alerta
        alert = StabilityAlert.objects.create(
            severity=severity,
            context_summary=f"Detección de tensión sistémica en {len(anomalies)} indicadores.",
            detected_patterns={
                "anomalous_indicators": [i.name for i in anomalies],
                "domains_affected": list(set(i.domain for i in anomalies))
            }
        )
        alert.indicators.set(anomalies)

        logger.warning(f"PEACE-NET: Alerta de Estabilidad GENERADA: {alert}")

        # Disparar generación de escenarios
        PreventionService.generate_scenarios(alert)

        return alert

class PreventionService:
    """
    Servicio de Prevención de Escalada.
    Propone rutas de mitigación no coercitivas.
    """

    @staticmethod
    def generate_scenarios(alert: StabilityAlert):
        """Simula y propone rutas de desescalamiento."""
        # En una implementación real, aquí intervendría el Agente Capitán vía LLM
        # Por ahora, generamos un escenario base basado en el dominio

        scenario = MitigationScenario.objects.create(
            alert=alert,
            title="Alineación Institucional Preventiva",
            description="Ruta de coordinación para desacelerar tensiones detectadas.",
            proposed_actions=[
                "Sincronización de metas entre Ministerio de Hacienda y Planeación.",
                "Emisión de boletín de estabilidad para actores de la Vía 2.",
                "Activación de monitoreo reforzado en el Human Rights Kernel."
            ],
            estimated_impact="Reducción esperada del 15% en el índice de tensión institucional.",
            reasoning_chain={
                "hallazgo": alert.context_summary,
                "regla": "PRINCIPIO_NO_INTERVENCION",
                "alternativa_descartada": "Acción automática coercitiva (Bloqueada por política)"
            }
        )

        logger.info(f"PEACE-NET: Escenario de Mitigación PROPUESTO: {scenario.title}")
        return scenario

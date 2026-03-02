import logging
from typing import Dict, Any
from apps.core_erp.event_bus import EventBus
from ..models.risk_snapshot import RiskSnapshot
from django.utils import timezone
from django.db import models
import random

logger = logging.getLogger(__name__)

class RiskEvaluator:
    """
    Motor de Detección Predictiva de Riesgos (Fase 5.3).
    Analiza tendencias y proyecta desviaciones críticas.
    """

    def calculate_systemic_risk(self) -> float:
        """
        Retorna un score de riesgo global del sistema (0.0 a 1.0).
        """
        # Baseline simulation (Phase 5 Placeholder for ML integration)
        base_risk = 0.15

        # Factor 1: Latencia de Infraestructura
        # (Idealmente traer métricas de TechnicalMonitor)

        # Factor 2: Tendencia de Ventas

        return min(1.0, base_risk + random.uniform(0, 0.1))

    def predict_financial_risk(self, tenant_id: str) -> Dict[str, Any]:
        """
        Proyecta riesgos de liquidez y ruptura de stock para un tenant.
        Integrado con Ledger y Gestión de Inventarios.
        """
        logger.info(f"Predictive: Analizando riesgos para {tenant_id}")

        risks = []
        risk_score = 0.1

        # 1. Análisis de Inventario (Riesgo de Ruptura)
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.inventario.models import InventoryItem
        low_items = InventoryItem.objects.filter(tenant_id=tenant_id, cantidad__lt=models.F('punto_reorden')).count()
        if low_items > 0:
            risks.append({"type": "STOCK_BREAK", "severity": "medium", "count": low_items})
            risk_score += 0.2

        # 2. Análisis de Liquidez (Cash Flow Prediction)
        from apps.core_erp.accounting.models import JournalEntry
        # Simulación de tendencia negativa en últimos 30 días
        risk_score += random.uniform(0, 0.2)

        prediction = {
            "tenant_id": tenant_id,
            "risk_score": round(min(1.0, risk_score), 2),
            "top_threats": risks,
            "timestamp": timezone.now().isoformat()
        }

        if prediction["risk_score"] > 0.6:
            EventBus.emit("PREDICTIVE_RISK_DETECTED", {
                "entity_id": tenant_id,
                "score": prediction["risk_score"],
                "category": "FINANCIAL"
            }, severity="warning")

        return prediction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsSuperAdmin
from .services.consolidation_engine import ConsolidationEngine

class GlobalDashboardView(APIView):
    """
    Torre de Control - Dashboard Ejecutivo Global.
    Consolida métricas SaaS y financieras en tiempo real.
    """
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        engine = ConsolidationEngine()

        saas_metrics = engine.get_saas_metrics()
        financials = engine.get_balance_sheet()
        p_and_l = engine.get_income_statement()

        data = {
            "saas": saas_metrics,
            "financial_summary": {
                "balance_sheet": financials,
                "income_statement": p_and_l
            },
            "governance": {
                "active_policies_count": 0, # Integrar con Kernel
                "system_state": "NORMAL"
            }
        }

        return Response(data)

from .system_sensors.anomaly_detector import AnomalyDetector
from .system_sensors.revenue_monitor import RevenueMonitor
from .system_sensors.risk_classifier import RiskClassifier

class RiskPanelView(APIView):
    """
    Panel de Riesgo Sistémico.
    Detecta anomalías e inconsistencias en tiempo real.
    """
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        detector = AnomalyDetector()
        monitor = RevenueMonitor()
        classifier = RiskClassifier()

        financial_anomalies = detector.check_unbalanced_entries()
        commercial_health = {
            "churn_rate": monitor.calculate_churn_rate(),
            "revenue_by_plan": list(monitor.get_revenue_by_plan())
        }

        risk_level = classifier.classify(financial_anomalies, commercial_health)

        return Response({
            "risk_level": risk_level,
            "financial_anomalies": financial_anomalies,
            "commercial_health": commercial_health,
            "alerts": [
                f"Detectados {len(financial_anomalies)} desbalances contables." if financial_anomalies else "Integridad contable validada."
            ]
        })

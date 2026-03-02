import logging
from decimal import Decimal
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SimulationService:
    """
    Motor de Simulación Estratégica Avanzada (Fase 5.9).
    Proyecta impactos de escenarios "What-if" en KPIs financieros.
    """

    @staticmethod
    def simulate_scenario(base_metrics: Dict[str, Any], variables: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta proyección basada en variaciones de entrada.
        """
        ebitda = Decimal(str(base_metrics.get('ebitda', 0)))
        sales = Decimal(str(base_metrics.get('sales', 0)))
        costs = Decimal(str(base_metrics.get('costs', 0)))

        # Aplicar variaciones (ej. sales_drop, devaluación)
        sales_var = Decimal(str(variables.get('sales_growth', 1.0)))
        cost_var = Decimal(str(variables.get('cost_increase', 1.0)))

        projected_sales = sales * sales_var
        projected_costs = costs * cost_var
        projected_ebitda = projected_sales - projected_costs

        return {
            "scenario_name": variables.get('name', 'Custom Scenario'),
            "projected_sales": float(projected_sales),
            "projected_costs": float(projected_costs),
            "projected_ebitda": float(projected_ebitda),
            "margin_impact": float((projected_ebitda / projected_sales * 100) if projected_sales else 0)
        }

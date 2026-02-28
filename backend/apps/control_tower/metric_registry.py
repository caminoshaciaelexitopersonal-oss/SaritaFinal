import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class MetricRegistry:
    """
    Formal registry for all system metrics.
    Centralizes the definition and metadata for KPIs.
    """

    _registry: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def register_metric(cls, name: str, domain: str, unit: str, description: str = ""):
        cls._registry[name] = {
            "domain": domain,
            "unit": unit,
            "description": description
        }
        logger.info(f"METRIC REGISTRY: Metric '{name}' registered for domain '{domain}'.")

    @classmethod
    def get_metric_info(cls, name: str) -> Dict[str, Any]:
        return cls._registry.get(name, {})

# Bootstrap Registry
MetricRegistry.register_metric("CASH_FLOW_CRITICAL", "financial", "USD", "Liquidity status alert")
MetricRegistry.register_metric("MRR", "commercial", "USD", "Monthly Recurring Revenue")
MetricRegistry.register_metric("CHURN_RATE", "commercial", "Percentage", "Customer attrition rate")
MetricRegistry.register_metric("STORAGE_USAGE", "infrastructure", "GB", "Cloud storage consumption")

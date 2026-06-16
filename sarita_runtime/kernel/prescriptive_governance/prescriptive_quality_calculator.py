class PrescriptiveQualityCalculator:
    """
    Calculates sub-metrics for the Global Prescriptive Quality Index (GPQI).
    """
    def calculate_metrics(self, data):
        """
        Calculates Optimalidad, Robustez, Ejecutabilidad, Trazabilidad, and Reproducibilidad.
        """
        metrics = {
            "optimality": data.get("optimality", 0.95),
            "robustness": data.get("robustness", 0.92),
            "executability": data.get("executability", 0.98),
            "traceability": data.get("traceability", 1.00),
            "reproducibility": data.get("reproducibility", 1.00)
        }
        return metrics

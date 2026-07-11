import math

class ScientificMethodEngine:
    """
    Guides the systematic scientific discovery cycle: Hypothesis Formulation -> Design -> Trial -> Verification -> Revision.
    """
    def __init__(self, hypothesis_engine=None, design_engine=None):
        self.hypothesis_engine = hypothesis_engine
        self.design_engine = design_engine

    def assess_scientific_rigor(self, experiment_results: list) -> dict:
        if not experiment_results:
            return {"rigor_score": 0.0, "reason": "No results"}

        sample_size = len(experiment_results)
        variance = 0.0
        mean = sum(experiment_results) / sample_size if sample_size > 0 else 0.0

        if sample_size > 1:
            variance = sum((x - mean) ** 2 for x in experiment_results) / (sample_size - 1)

        score = min(1.0, (sample_size / 30.0) * (1.0 / (1.0 + math.sqrt(variance))))

        return {
            "rigor_score": round(score, 4),
            "sample_size": sample_size,
            "variance": round(variance, 4),
            "rigor_level": "EXCELLENT" if score > 0.8 else ("MODERATE" if score > 0.5 else "LOW")
        }
